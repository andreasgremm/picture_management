import datetime as dt
import pathlib
import exiftool
import os
import subprocess
from itertools import chain
from tzlocal import get_localzone

local_tz = get_localzone()

files = [f for f in chain(pathlib.Path().glob("*.JPG"), pathlib.Path().glob("*.jpg"), pathlib.Path().glob("*.jpeg"), pathlib.Path().glob("*.MOV"), pathlib.Path().glob("*.mp4"))]

for file in files:
    status=os.stat(file)
    birth=dt.datetime.fromtimestamp(status.st_birthtime).astimezone(local_tz)
    print(file, birth)
    with exiftool.ExifToolHelper() as et:
        metadata = et.get_metadata([file])
        if metadata[0]["File:FileType"] in ["MP4", "MOV"]:
            date_name = "CreationDate"
            if "QuickTime:CreationDate" not in metadata[0]:
                result = et.execute(
                    *[
                        f"-quicktime:CreationDate={birth.isoformat()}",
                        "-m",
                        file,
                    ]
                )
        elif metadata[0]["File:FileType"] in ["PNG", "JPEG"]:
            date_name = "DateCreated"
            if "XMP:DateCreated" not in metadata[0]:
                result = et.execute(
                    *[
                        f"-xmp:datecreated={birth.isoformat()}",
                        "-m",
                        file,
                    ]
                )
    final_path = birth.strftime("%Y/%Y_%m")
    name_prefix = birth.strftime("%Y_%m_%d-%H_%M_%S")
    destination_filename = f"{name_prefix}-{file}"
    try:
        exiftool_output = subprocess.run(
            [
                "exiftool",
                "-P",
                f"-FileName<{date_name}",
                "-d",
                f"{final_path}/{destination_filename}",
                "-m",
                file,
            ],
            capture_output=True,
            text=True,
            check=False,
        )
    except Exception as e:
        print(e)

