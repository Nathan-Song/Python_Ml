
# Python Schulung

## Klassenabstraktion und -hierarchien in Python

In Python sind Klassen das zentrale Mittel zur Strukturierung von Code, der auf Objektorientierung basiert. Die Konzepte der Abstraktion und der Klassenhierarchie ermöglichen es Entwicklern, komplexe Systeme übersichtlich und modular zu gestalten.

## Kernkonzepte

### Klassen und Objekte

Eine Klasse definiert eine Blaupause für Objekte. Objekte sind Instanzen von Klassen, die die in der Klasse definierten Eigenschaften und Methoden besitzen.

```python
class Fahrzeug:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def starten(self):
        print(f"{self.marke} {self.modell} startet.")

auto = Fahrzeug("Toyota", "Corolla")
auto.starten()
```

### Vererbung

Vererbung ermöglicht es einer Klasse, Eigenschaften und Methoden einer anderen Klasse zu erben. Dies fördert die Wiederverwendung von Code und ermöglicht die Bildung von Klassenhierarchien.

```python
class Auto(Fahrzeug):
    def __init__(self, marke, modell, anzahl_tueren):
        super().__init__(marke, modell)
        self.anzahl_tueren = anzahl_tueren

    def anzeigen(self):
        print(f"Auto: {self.marke} {self.modell}, Türen: {self.anzahl_tueren}")

mein_auto = Auto("BMW", "3er", 4)
mein_auto.anzeigen()
```

### Abstrakte Klassen

Abstrakte Klassen dienen als Vorlage für andere Klassen und können nicht instanziiert werden. Sie enthalten mindestens eine abstrakte Methode, die in den abgeleiteten Klassen implementiert werden muss.

```python
from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def geraeusch_machen(self):
        pass

class Hund(Tier):
    def geraeusch_machen(self):
        print("Wuff!")

hund = Hund()
hund.geraeusch_machen()
```

### Polymorphismus

Polymorphismus erlaubt es, Objekte unterschiedlichster Klassen auf die gleiche Weise zu behandeln, solange sie eine gemeinsame Schnittstelle oder Basisklasse haben.

```python
class Katze(Tier):
    def geraeusch_machen(self):
        print("Miau!")

def tier_geraeusch(tier: Tier):
    tier.geraeusch_machen()

hund = Hund()
katze = Katze()

tier_geraeusch(hund)
tier_geraeusch(katze)
```

## Praktische Anwendung

In der Praxis ermöglicht die Nutzung von Klassenabstraktion und -hierarchien die Entwicklung robuster und flexibler Anwendungen. Diese Konzepte sind besonders nützlich in der Softwareentwicklung, bei der komplexe Systeme in einfache, wiederverwendbare Komponenten zerlegt werden müssen.

### Beispielprojekt: Verwaltungssystem für Fahrzeuge

- Basisklasse: `Fahrzeug`
- Abgeleitete Klassen: `Auto`, `Motorrad`, `LKW`
- Nutzung von Polymorphismus: Einheitliche Behandlung der verschiedenen Fahrzeugtypen im System

## Fazit

Klassenabstraktion und -hierarchien sind grundlegende Konzepte der objektorientierten Programmierung in Python. Das Verständnis und die Anwendung dieser Techniken sind entscheidend für die Entwicklung wartbarer und skalierbarer Software.
