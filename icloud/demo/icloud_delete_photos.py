# source_album = 'Test'
# photo = next(iter(api.photos.albums[source_album]), None)

latest_delete_date = dt.datetime(2025,12,1).astimezone(local_tz)

destination_path = f"{Path.home()}/Bilder/iCloud_Mediathek"
photo_nr = 0
anz_photos_deleted = 0

photo_list = []

for photo in api.photos.albums[source_album]:
    photo_nr += 1
    print(f"Working on {photo.filename} - Nummer {photo_nr}:")
    if (photo.__dict__["_asset_record"]["fields"]["isFavorite"]["value"] == 0) and (photo.created < latest_delete_date):
        photo_name_base = photo.filename.rsplit(".", 1)[0]
        photo_info_file = glob.glob(f"{destination_path}/*{photo_name_base}.json")
        if len(photo_info_file) > 0:
            with open(photo_info_file[0], "r") as infofile:
                info_data = json.load(infofile)
                if info_data[0]["recordName"] == photo.id:
                    print(f"      Mark Media: {photo.id}, {photo.filename}")
                    # photo_deleted = photo.delete()
                    photo_list.append(photo)
                    # print(f"      Media deleted: {photo_deleted}")
                    time.sleep(0.1)
                    anz_photos_deleted += 1
    print(f"   Finished: {photo.filename}\n")

print(f"Photos Anzahl: # {photo_nr}\n")
print(f"Photos markiert: # {anz_photos_deleted}\n")

for i, photo in enumerate(photo_list):
    print(f"Delete Media: {photo.id}, {photo.filename} - Nummer {i+1}:")
    photo_deleted = photo.delete()
    print(f"   Media deleted: {photo_deleted}")
    time.sleep(0.5)

