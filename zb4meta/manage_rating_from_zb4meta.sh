#!/bin/bash

basepath=$(pwd)

while read metainfo
do
  # echo "$metainfo"
  fullpath="$basepath"/"$metainfo"
  finalpath=$(dirname "$fullpath")
  cd "$finalpath"
  pwd
  dos2unix -n zb4meta.info zb4metainfo_dos2unix.xml
  sed  -e'1i <?xml version="1.0" encoding="UTF-8"?>\n<root>' -e '$a </root>' zb4metainfo_dos2unix.xml| \
  sed -e's/<item:\(.*\)>/<item filename="\1">/' -e's-</item:.*>-</item>-' >temp.xml

  while read line
  do
    filename=$(cut -f1 <<<$line)
    rating=$(cut -f2 <<<$line)
    echo "$line"'|'"$filename"'|'"$rating"
    exiftool -P -overwrite_original -Rating=${rating//\"/} "$filename"
  done < <(paste <(xmllint --xpath "//item/@filename" temp.xml | grep -oP '(?<=")[^"]+') \
         <(xmllint --xpath "//item/Favourite_Photo/text()" temp.xml))

done < Alle_zb4meta_info.txt
# <(find . -name zb4meta.info | sed -e's/ /\\ /g' )
