import datetime as dt
import glob
import json
import time
from pathlib import Path

from pyicloud import PyiCloudService
from tzlocal import get_localzone


def delete_photos(
    api: PyiCloudService,
    source_album: str,
    destination_path: str = f"{Path.home()}/Bilder/iCloud_Mediathek",
    latest_date: tuple = (2025, 12, 1),
) -> tuple:
    # source_album = 'Test'
    # photo = next(iter(api.photos.albums[source_album]), None)
    # destination_path = f"{Path.home()}/Bilder/iCloud_Mediathek"

    # latest_delete_date = dt.datetime(2025,12,1).astimezone(local_tz)
    local_tz = get_localzone()
    latest_delete_date: dt.datetime = dt.datetime(
        latest_date[0], latest_date[1], latest_date[2]
    ).astimezone(local_tz)
    photo_nr = 0
    anz_photos_deleted = 0

    photo_list = []

    for photo in api.photos.albums[source_album]:
        photo_nr += 1
        print(f"Working on {photo.filename} - Nummer {photo_nr}:")
        if (photo.__dict__["_asset_record"]["fields"]["isFavorite"]["value"] == 0) and (
            photo.created < latest_delete_date
        ):
            photo_name_base = photo.filename.rsplit(".", 1)[0]
            photo_info_file = glob.glob(f"{destination_path}/*{photo_name_base}.json")
            if len(photo_info_file) > 0:
                with open(photo_info_file[0], "r") as infofile:
                    info_data = json.load(infofile)
                    if info_data[0]["recordName"] == photo.id:
                        print(f"      Mark Media: {photo.id}, {photo.filename}")
                        photo_list.append(photo)
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

    return (photo_nr, anz_photos_deleted)
