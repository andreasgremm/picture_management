import pathlib
import exiftool
import subprocess
from itertools import chain

files = [f for f in chain(pathlib.Path().glob("*.JPG"), pathlib.Path().glob("*.jpg"), pathlib.Path().glob("*.jpeg"), pathlib.Path().glob("*.MOV"), pathlib.Path().glob("*.mp4"))]
# files = ["3101d228-bd3f-488d-a0dc-d2c1d5131c22.jpg", "a37a3f12-03bc-49a7-85f0-36e7be53daa4.mp4"]
with exiftool.ExifToolHelper() as et:
    metadata = et.get_metadata(files)
    for d in metadata:
        if d['File:FileType'] in ['MP4', 'MOV']:
            if "QuickTime:CreateDate" in d:
                print("{:20.20} {:20.20}".format(d["SourceFile"],
                                                d["QuickTime:CreateDate"]))
                # exiftool  '-Directory<DateTimeOriginal' -d %Y/%m 2025_12_07-17_24_08-a37a3f12-03bc-49a7-85f0-36e7be53daa4.mp4
                # result=exiftool.ExifToolHelper().execute(*["-P", "-Directory<DateCreated",  "-d", "%Y/%m", d["SourceFile"]])
                exiftool_output = subprocess.run(["exiftool", "-Directory<CreateDate", "-d", "%Y/%Y_%m", "-m", d["SourceFile"]], capture_output=True, text=True, check=False)           
        elif d['File:FileType'] in ['PNG', 'JPEG']:
            if "EXIF:CreateDate" in d:
                print("{:20.20} {:20.20}".format(d["SourceFile"],
                                                d["EXIF:CreateDate"]))
                # exiftool  '-Directory<DateTimeOriginal' -d %Y/%m 2025_12_07-17_24_08-a37a3f12-03bc-49a7-85f0-36e7be53daa4.mp4
                # result=exiftool.ExifToolHelper().execute(*["-P", "-Directory<DateCreated",  "-d", "%Y/%m", d["SourceFile"]])
                exiftool_output = subprocess.run(["exiftool", "-Directory<CreateDate", "-d", "%Y/%Y_%m", "-m", d["SourceFile"]], capture_output=True, text=True, check=False)
