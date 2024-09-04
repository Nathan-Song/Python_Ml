
# Python Schulung: Klassenvererbung

## Einführung

In dieser Schulungseinheit beschäftigen wir uns mit der Klassenvererbung in Python, einem Kernkonzept der objektorientierten Programmierung. Klassenvererbung ermöglicht es, Eigenschaften und Methoden von einer bestehenden Klasse auf eine neue Klasse zu übertragen, was den Code wiederverwendbar und wartbar macht.

## Grundlagen der Vererbung

### Definition einer Basisklasse

Eine Basisklasse definiert Eigenschaften und Methoden, die von anderen Klassen wiederverwendet werden können.

```python
class Fahrzeug:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def anzeigen(self):
        print(f'Fahrzeug: {self.marke} {self.modell}')
```

### Erstellen einer abgeleiteten Klasse

Eine abgeleitete Klasse erbt Eigenschaften und Methoden von der Basisklasse und kann zusätzliche Eigenschaften oder Methoden hinzufügen.

```python
class Auto(Fahrzeug):
    def __init__(self, marke, modell, kraftstoffart):
        super().__init__(marke, modell)
        self.kraftstoffart = kraftstoffart

    def details_anzeigen(self):
        self.anzeigen()
        print(f'Kraftstoffart: {self.kraftstoffart}')
```

## Gute Praktiken bei der Vererbung

### Verwendung von `super()`

Die `super()` Funktion in Python ermöglicht es, Methoden der Basisklasse aufzurufen und stellt sicher, dass die Initialisierung der Basisklasse korrekt erfolgt.

### Überschreiben von Methoden

Das Überschreiben von Methoden in der abgeleiteten Klasse sollte sorgfältig durchgeführt werden, um die Funktionalität der Basisklasse zu erweitern oder anzupassen, ohne sie zu beeinträchtigen.

### Vermeidung von Mehrfachvererbung

Mehrfachvererbung sollte vermieden werden, wenn sie zu Komplikationen oder Unklarheiten im Vererbungshierarchie führen kann. Stattdessen sollte Komposition bevorzugt werden.

## Beispiel: Erweiterung der Fahrzeugklasse

```python
class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, hat_beiwagen):
        super().__init__(marke, modell)
        self.hat_beiwagen = hat_beiwagen

    def motorrad_details(self):
        self.anzeigen()
        print('Beiwagen vorhanden:' if self.hat_beiwagen else 'Kein Beiwagen')
```

## Fazit

Die korrekte Anwendung der Klassenvererbung in Python kann die Entwicklung effizienter und klar strukturierter Anwendungen erheblich erleichtern. Es ist wichtig, die Prinzipien der guten Vererbungspraxis zu verstehen und anzuwenden.
