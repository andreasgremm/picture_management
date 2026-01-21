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
7. Bereitstellen der Python Snippets.  
`cp -r "$repoverzeichnis"/demo .`

Das Ergebnis ist folgende Verzeichnisstruktur:

```text
.
├── demo
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
3. Herunterladen und Bearbeiten der Bilder.
    * Öffnen der Datei **demo/icloud_download_photos.py** in einem Editor.
    * Den Inhalt in die Zwischenablage kopieren
    * Die Zwischenablage beim Python-Prompt einfügen und mit "\<Enter\>" starten.  
    Dieser Schritt wird in einer späteren Version möglicherweise durch den Aufruf einer Python-Methode ersetzt.
