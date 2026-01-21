# source_album = 'Test'
# photo = next(iter(api.photos.albums[source_album]), None)
destination_path = f"{Path.home()}/Bilder/iCloud_Mediathek"
Path(destination_path).mkdir(parents=True, exist_ok=True)

photo_nr = 1
for photo in api.photos.albums[source_album]:
    print(f"Working on {photo.filename} - Nummer {photo_nr}:")
    date_out_str = photo.created.astimezone(local_tz).strftime("%Y%m%d%H%M.%S")
    name_prefix = photo.created.astimezone(local_tz).strftime("%Y_%m_%d-%H_%M_%S")
    destination_filename = f"{name_prefix}-{photo.filename}"
    complete_file_name = f"{destination_path}/{destination_filename}"
    final_path = (
        f'{destination_path}/{photo.created.astimezone(local_tz).strftime("%Y/%Y_%m")}'
    )
    with open(complete_file_name, "wb") as opened_file:
        transfered_bytes = opened_file.write(photo.download("original"))
    with open(f"{Path(complete_file_name).with_suffix('.json')}", "w") as asset_info:
        transfered_bytes = asset_info.write(
            json.dumps(photo.__dict__["_master_record"], indent=2)
        )
        transfered_bytes = asset_info.write(
            json.dumps(photo.__dict__["_asset_record"], indent=2)
        )
        transfered_bytes = asset_info.write(
            json.dumps(photo.__dict__["_versions"], indent=2)
        )
    rating = 0
    with exiftool.ExifToolHelper() as et:
        if photo.__dict__["_asset_record"]["fields"]["isFavorite"]["value"] != 0:
            rating = 5
            # result = et.execute(*["-Rating=5", complete_file_name])
        metadata = et.get_metadata([complete_file_name])
        # if metadata[0]["File:FileType"] in ["MP4", "MOV"]:
        if photo.item_type == 'movie':
            date_name = "CreationDate"
            if "QuickTime:CreationDate" not in metadata[0]:
                result = et.execute(
                    *[
                        f"-quicktime:CreationDate={photo.created.isoformat()}",
                        "-m",
                        complete_file_name,
                    ]
                )
        # elif metadata[0]["File:FileType"] in ["PNG", "JPEG"]:
        elif photo.item_type == 'image':
            date_name = "DateCreated"
            if "XMP:DateCreated" not in metadata[0]:
                # datetime.datetime.now(datetime.timezone.utc).isoformat()
                result = et.execute(
                    *[
                        f"-xmp:datecreated={photo.created.isoformat()}",
                        "-m",
                        complete_file_name,
                    ]
                )
    touch_output = subprocess.run(
        ["touch", "-a", "-m", "-t", date_out_str, complete_file_name],
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        exiftool_output = subprocess.run(
            [
                "exiftool",
                "-P",
                f"-FileName<{date_name}",
                "-d",
                f"{final_path}/{destination_filename}",
                "-m",
                f"-Rating={rating}",              
                complete_file_name,
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        result = et.execute(
                    *[
                        f"-xmp:TagsList+=iCloud:{source_album}",
                        "-m",
                        "-P",
                        "-overwrite_original",
                        f"{final_path}/{destination_filename}",
                    ]
                )
    except Exception as e:
        print(e)
    photo_nr += 1
    print(f"   Finished: {photo.filename}\n")
