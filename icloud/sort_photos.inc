exiftool -P -m "-CreateDate<FileModifyDate" *.jpeg *.tif *.JPG *.mp4 *.jpg
exiftool -P -m "-Directory<CreateDate" -d "%Y/%Y_%m" *.jpeg *.tif *.JPG *.mp4 *.jpg
