import click
from pyicloud import PyiCloudService


def select_album(api: PyiCloudService) -> str:
    for i, album in enumerate(api.photos.albums):
        print("  %s: %s" % (i, album.name))
    source_album_nr = click.prompt("Which album would you like to use?", default=0)
    return api.photos.albums[source_album_nr].name

    # print(source_album)
    # for photo in api.photos.albums['Screenshots']:
    #     print(photo, photo.filename, photo.asset_date, photo.created)
