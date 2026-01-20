# Manage Rating from zb4meta.info

Ratings vom Cannon ZoomBrowser Programm liegen in der Datei zb4meta.info in einem Pseudo-XML vor.

Ohne dem entsprechenden Programm werden diese vergebenen Ratings wertlos.

Es gibt Programme im Internet, die interaktiv jeweils eine Datei/Verzeichnis auswählen lässt, um die dahinterliegenden Info-Dateien auszuwerten und die Exif-Daten der genannten Bilder zu schreiben.

Das Problem: Dieses Windows-Programm lässt sich nur mit Hilfsmitteln unter Linux oder MacOS aufrufen, bestimmte Windows-Dateinamenskonventionen führen unter Non-Windows-Systemen zu Abbrüchen. 

Daher liefert das Shell-Script *manage_ranting_from_zb4meta.sh* eine Möglichkeit iterativ durch eine Verzeichnisstruktur die Exif-Daten der Bilder mit den im Zoombrowser vergebenen Ratings zu versehen.

Da sich trotzdem immer wieder Verzeichnisnamensprobleme ergeben haben ist dieser Prozess im besten Fall Zweistufig durchzuführen.

* Erzeugen einer Steuerliste
```shell
find . -name zb4meta.info | sed -e's/ /\\ /g' ) >Alle_zb4meta_info.txt
```
* Abarbeiten der Steuerliste durch das Script.

Wenn es sicher keine Verzeichnis-Namens-Probleme gibt, dann dieses auch in einem, dem oben erwähnten zweiten Schritt erfolgen, und nur das Shell-Skript ausgeführt werden. Dafür muss die letzte aktive Zeile des Scriptes ausgetauscht werden.

```shell
done < Alle_zb4meta_info.txt
# <(find . -name zb4meta.info | sed -e's/ /\\ /g' )

### muss getauscht werden gegen:
done <(find . -name zb4meta.info | sed -e's/ /\\ /g' )
# <(find . -name zb4meta.info | sed -e's/ /\\ /g' )
```
