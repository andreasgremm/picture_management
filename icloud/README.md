# Verwaltung von Messenger-Medien aus der iCloud

## Installation

1. Clone dieses Repositories an eine gewünschte Stelle. Nennen wir dieses **repoverzeichnis**.
2. Als Basis wird das Tool *PyiCloud* benötigt, das Repository sollte ebenfalls an eine gewünschte Stelle gecloned werden. Nennen wir dieses **pyicloudverzeichnis**.  
`git clone https://github.com/timlaing/pyicloud.git`
3. Anlage eines Basisverzeichnis für unsere Aktivität, nennen wir dieses **icloud**.  
`mkdir -p "$icloud"; cd "$icloud"`
4. Erstellen eines Python Virtuellen Environments.  
`python3.<Version> -m venv pyenv`
5. Aktivieren des Environment und Installation der Python Requirements

    ```bash
    source ./pyenv/bin/activate
    pip install --upgrade pip
    pip install -r "$repoverzeichnis"/icloud/requirements.txt
    deactivate
    ```

6. Bereitstellen der pyicloud Routinen.
`cp -r "$pyicloudverzeichnis"/pyicloud .`
7. Bereitstellen der Python Module.  
`cp -r "$repoverzeichnis" .`

Das Ergebnis ist folgende Verzeichnisstruktur:

```text
.
├── pyenv
└── pyicloud
```

## Nutzung

Die Nutzung des Tools wird aktuell durch den Aufruf der Python-Snippets realisiert.

1. Vorbereiten der Umgebung  

    ```shell
    source ./pyenv/bin/activate
    python
    ```

2. Authentifizieren und Auswahl des zu betrachtenden Albums  

    ```python
    from demo.pyicloud_auth import *
    ```

    In diesem Schritt werden die Zugangsdaten zum iCloud-Account abgefragt und die Zwei-Faktor Authentifizierung durchgeführt.  
    Danach werden die zugänglichen Alben aufgelistet und abgefragt welches Album verwendet werden soll.  
    Dieser Schritt wird in einer späteren Version möglicherweise durch den Aufruf einer Python-Methode ersetzt.

3. Herunterladen und Bearbeiten der Bilder aus der iCloud.
    * Aufruf des Moduls **download_photos**
  
    ```python
    # Schnittstelle von download_photos
    download_photos.__annotations__
    {'api': <class 'pyicloud.base.PyiCloudService'>, 'source_album': <class 'str'>, 'destination_path': <class 'str'>, 'return': <class 'int'>}

    # Aufrufbeispiel
    anzahl_photos_geladen = download_photos(api, source_album)
    ```

4. Kopieren der Bilder an ihr Zielort  
   Dieser Schritt ist sehr abhängig davon, wo der Zielort ist. Daher gebe ich hier keine Vorgehensweise vor.

5. Überprüfen der Daten
   Liegen die Daten an der richtigen Stelle, gibt es ein Backup der heruntergeladenen Daten.

6. Löschen der Bilder in der iCloud
   * Aufruf des Moduls **delete_photos**

    ```python
    # Schnittstelle von delete_photos:
    delete_photos.__annotations__
    {'api': <class 'pyicloud.base.PyiCloudService'>, 'source_album': <class 'str'>, 'destination_path': <class 'str'>, 'latest_date': <class 'tuple'>, 'return': <class 'tuple'>}
    
    # Aufrufbeispiel
    anzahl_photos, geloeschte_photos = delete_photos(api, source_album, latest_date=(2025,11,1)
    ```

7. Ändern des Albums
   * Aufruf des Moduls **select_album**
  
    ```python
    # Schnittstelle von select_album:
    select_album.__annotations__
    {'api': <class 'pyicloud.base.PyiCloudService'>, 'return': <class 'str'>}

    # Aufrufbeispiel
    source_album=select_album(api)
    ```
