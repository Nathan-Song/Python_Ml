
# Python Schulung: Objekte erstellen und initialisieren

## Einführung

In Python ist alles ein Objekt, von einfachen Datenstrukturen bis zu komplexen Funktionen. Das Verstehen, wie man Objekte erstellt und initialisiert, ist ein grundlegender Aspekt der Python-Programmierung.

## Grundlagen der Objekterstellung in Python

### Klassen definieren

Eine Klasse in Python definiert die Struktur und das Verhalten von Objekten. Hier ist ein einfaches Beispiel einer Klasse, die ein Auto darstellt.

```python
class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def display_info(self):
        print(f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}")
```

### Objekte initialisieren

Objekte werden durch Aufrufen der Klasse initialisiert, wobei die erforderlichen Daten als Argumente übergeben werden.

```python
mein_auto = Auto('Toyota', 'Corolla', 2021)
mein_auto.display_info()
```

## Praktische Anwendung

### Beispielprojekt: Bibliotheksverwaltungssystem

- Objekte für Bücher, Nutzer und Ausleihvorgänge erstellen.
- Methoden zur Verwaltung von Buchbeständen und Benutzerausleihen.

```python
class Buch:
    def __init__(self, titel, autor, isbn):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

class Bibliothek:
    def __init__(self):
        self.buecher = []

    def buch_hinzufuegen(self, buch):
        self.buecher.append(buch)

    def buch_zeigen(self):
        for buch in self.buecher:
            print(f"Buch: {buch.titel}, Autor: {buch.autor}")
```

## Fazit

Das Erstellen und Initialisieren von Objekten in Python ermöglicht es Entwicklern, strukturierte und skalierbare Anwendungen zu bauen. Durch die Praxisbeispiele wird das Verständnis dieser Konzepte gefestigt und vertieft.
