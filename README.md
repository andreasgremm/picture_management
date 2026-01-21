# Picture Management

In diesem Verzeichnis liegen ein paar Tools, um EXIF-Daten für die Verwaltung vom Bilder- und Videodateien zu nutzen.

Die ursprüngliche Problemstellung war, die Situation, dass Whatsapp-Bilder/Videos aus der Apple-iCloud auf die lokale Festplatte geladen wurde oder Media-Dateien von alten Handys (Samsung, Blackberry) auf Festplatte gesichert wurden.

Diese Dateien lagen in "wilden Ordnerstrukturen" auf der Festplatte vor, ein Verzeichnis pro Sicherung/Download mit keiner zeitlichen Zuordnung. Oft waren auch nur die Betriebssystemdaten zu "Erstellung" oder "Modifikation" der Dateien ein Hinweis auf deren Erzeugungsdatum.

Die Situation, dass sich weiter Dateien aus Messengern wie WhatsApp/Signal/... in der iCloud ansammeln und dort im wesentlichen zu erhöhten Speicherkosten führen, aber eine Kopie per "Fotos"-App auf Festplatte zu einer Verfälschung der Erzeugungsdaten führt ist weiterhin akut.

Eine bestehende Mediensammlung, unter anderem von einer Canon-Kamera, wurde früher unter Windows mit dem Cannon Tool ZoomBrowser bearbeitet und insbesondere wurde mit diesem Tool ein Rating vergeben. Dieses Rating wurde vom ZoomBrowser jedoch nicht in den Exif-Daten sondern in einer separaten Datei hinterlegt. Diese separate Datei wurde mit dem Ende der Nutzung des Zoombrowsers nach einem Betriebssystemwechsel zu MacOS "wertlos".

Diese drei Problemstellungen habe ich mit einem Set an einfachen Tools gelöst.

## Sortieren von Mediadaten in Verzeichnissen

Für das Sortieren von Mediadateien in datumsspezifische Unterverzeichnisse gibt es zwei Ansätze.

1. Die Mediadateien haben keine relevanten mediatypischen EXIF-Daten, **aber die Betriebssystemdaten sind aussagekräftig**.  
In dieser Situation kann mit dem Script [sort_photos.inc](./icloud/demo/sort_photos.inc) die Exif-Daten aus den Betriebssytemdaten übernommen werden und die Mediadatei in ein datumsspezifisches Verzeichnis verschoben werden.
Existiert die Mediadatei bereits im Zielverzeichnis, wird sie dort nicht überschrieben.  
Das Script kann an andere Datei-Extensions angepasst werden und auch die Namensgebung der Verzeichnisstruktur kann den Wünschen angepasst werden.  
Der Aufruf erfolgt unter Linux aus dem Verzeichnis heraus, in dem die Mediadaten liegen. `source <Dateipfad>/sort_photos.inc`.

2. Die Mediadaten **haben** relevante mediatypischen EXIF-Daten.  
In diesem Fall kann entweder der zweite EXIFTOOL-Aufruf aus dem Script im vorherigen Kapitel, mit den relevanten EXIF-Daten getätigt werden, oder über das Python-Snippet [analyse_exifdate_from_mediafiles.py](./icloud/demo/analyse_exifdata_from_mediafiles.py) genutzt werden.  
Die Erweiterung dieses Snippets ermöglicht den Aufbau einer Informationsbasis. Hier ist nur Beispielhaft die Ausgabe von Metadaten-Informationen eingebaut.  
Meine Beobachtung war, dass die Exif-Daten mal ein "CreateDate", aber auch mal nur ein "ModifyDate" beinhalteten. Das Python-Snippet müsste entsprechend erweitert werden, ich habe dann nur temporär die Texte im Snippet entsprechend angepasst.

## Übernehmen der Rating-Informationen von ZoomBrowser

Das Tool zur Übernahme der Rating-Informationen liegt im Unterverzeichnis [zb4meta](./zb4meta/README.md) und ist dort auch beschrieben.

## Download von Messenger-Medien (und anderen) aus der iCloud mit Datumssortierung

Um Mediadateien aus der iCloud herunterladen zu können bedarf es einer Schnittstelle zur iCloud.

Hierzu nutze ich das hervorragend funktionierende API von [Tim Laing](https://github.com/timlaing).

Auf Basis dieses API's habe ich folgende Funktionen realisiert:

* Download der Mediadateien eines kompletten Albums
* Falls keine EXIF-Erzeugungsdaten vorhanden sind, werden diese auf Basis der iCloud-Informationen gesetzt.
* Wenn das Medium in der iCloud als "Favourite" markiert ist, wird das Rating auf "5" gesetzt. 
* Einsortieren der Dateien in eine datumsspezifische Verzeichnisstruktur (Falls die Datei dort noch nicht vorhanden ist).
* Ergänzen der Ergebnis-Media-Datei im Zielverzeichnis um ein Tag **iCloud:\<Source Album\>**.  
Alben in der iCloud sind virtueller Natur. Die Mediadatei besteht nur einmal in der iCloud, die Ablage in selbsterstellten Alben wird durch eine Referenz dargestellt.  
Das Endziel ist die Bereinigung der iCloud um die heruntergeladenen Medien, mit der Erweiterung der Taglist in den EXIF-Daten können die heruntergeladenen Bilder später wieder virtuellen Alben in anderen Tools zugewiesen werden.  
In dieser Version ermöglicht das Tool mehrere Durchläufe für alle selbst erstellten Alben, bevor die Daten aus der iCloud gelöscht werden.

Gedanken zum Löschen der Medien aus der iCloud. Wie beschrieben ist das eigentliche Ziel die Informationen aus den Messenger-Katalogen zu sichern und zu löschen.  
Aber eventuell sollen bestimmte Bilder in der MediaThek der iCloud erhalten bleiben.  
Der aktuelle Gedanke anhand des Beispielalbums "WhatsApp" ist folgender.

* Es existiert ein Album "WhatsApp", welches die aus WhatsApp empfangenen Medien beinhaltet.
* Im Verlauf des Lebenszyklus wurden eigene Alben nach Themen angelegt, Beispielsweise nach den Namen von Kindern/Enkeln ... mit einer Sammlung besonders gelungener Medien dieser Personen. Das gleiche Medium kann sich in unterschiedlichen Alben befinden, da mehrere Kinder/Enkel auf diesem Medium abgebildet sind.  
In selbsterstellten Alben befinden sich zusätzlich auch Medien aus der Hauptbibliothek, welche mit dem eigenen Handy aufgenommen wurden.
* Besonders schöne Medien wurden mit einem "Herz" als Favorit gekennzeichnet.

Im ersten Durchlauf werden die  Daten des Album "WhatsApp" heruntergeladen und, wie oben beschrieben, bearbeitet und in die gewünschte Verzeichnisstruktur einsortiert. Die nächsten Durchläufe verwenden die selbst erstellten Alben. Auch hier werden alle Daten heruntergeladen, bearbeitet und in der Verzeichnisstruktur abgelegt, falls noch nicht vorhanden.  
Sind alle selbsterstellten Alben so behandelt, können die Daten in den Zielordnern kontrolliert werden.

Ist das Ergebnis zufriedenstellend, können in einem Löschprozess die Medien aus dem Album "WhatsApp" gelöscht werden. Dieses löscht das Medium und seine Referenzen aus den selbstangelegten Alben. Eine Einschränkung könnte noch sein, dass entweder "junge Medien" und/oder "favorisierte Medien" nicht gelöscht werden.

Die Installation und Nutzung ist im Verzeichnis [iCloud](./icloud/README.md) beschrieben.
