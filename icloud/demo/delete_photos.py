# source_album = 'Test'
# photo = next(iter(api.photos.albums[source_album]), None)

destination_path = f"{Path.home()}/Bilder/iCloud_Mediathek"
photo_nr = 1

for photo in api.photos.albums[source_album]:
    print(f"Working on {photo.filename} - Nummer {photo_nr}:")
    if photo.__dict__["_asset_record"]["fields"]["isFavorite"]["value"] == 0:
        photo_name_base = photo.filename.rsplit(".", 1)[0]
        photo_info_file = glob.glob(f"{destination_path}/*{photo_name_base}.json")
        if len(photo_info_file) > 0:
            with open(photo_info_file[0], "r") as infofile:
                info_data = json.load(infofile)
                if info_data[0]["recordName"] == photo.id:
                    print(f"      Delete Kandidat {photo.id}")
    photo_nr += 1
    print(f"   Finished: {photo.filename}\n")
