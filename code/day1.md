
# Python Code Examples from Presentation

## Modul 1: Einführung in die Objektorientierung

### Lab 1.1: Grundlagen der Objektorientierung

#### Code 1: Erstellen einer Klasse und eines Objekts

```python
class Auto:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def get_info(self):
        return f"{self.marke} {self.modell} ({self.baujahr})"

# Beispielhafte Nutzung:
auto = Auto("Toyota", "Corolla", 2020)
print(auto.get_info())
```

### Lab 1.2: Objekte erstellen und initialisieren

#### Code 2: Validierung im Konstruktor

```python
class Product:
    def __init__(self, preis):
        if preis < 0:
            raise ValueError("Preis darf nicht negativ sein")
        self.preis = preis

# Beispielhafte Nutzung:
produkt = Product(100)
```

#### Code 3: Mehrere Objekte instanziieren

```python
class Fahrzeug:
    def __init__(self, typ, geschwindigkeit):
        self.typ = typ
        self.geschwindigkeit = geschwindigkeit

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

# Beispielhafte Nutzung:
auto = Fahrzeug("Auto", 50)
fahrrad = Fahrzeug("Fahrrad", 20)

auto.beschleunigen(10)
fahrrad.beschleunigen(5)
```

## Modul 2: Beziehungen zwischen Klassen

### Lab 2.1: Wie Klassen von anderen erben und wie man das richtig umsetzt

#### Code 4: Vererbung und Methodenüberschreibung

```python
class Tier:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return self.sound

class Hund(Tier):
    def make_sound(self):
        return f"{self.name} sagt Wuff!"

class Katze(Tier):
    def make_sound(self):
        return f"{self.name} sagt Miau!"

# Beispielhafte Nutzung:
hund = Hund("Bello", "Wuff")
katze = Katze("Mimi", "Miau")
print(hund.make_sound())
print(katze.make_sound())
```

### Lab 2.2: Aggregation und Komposition

#### Code 5: Aggregation Beispiel

```python
class Artikel:
    def __init__(self, name, preis):
        self.name = name
        self.preis = preis

class Einkaufsliste:
    def __init__(self):
        self.artikel = []

    def artikel_hinzufuegen(self, artikel):
        self.artikel.append(artikel)

    def gesamtpreis(self):
        return sum(artikel.preis for artikel in self.artikel)

# Beispielhafte Nutzung:
apfel = Artikel("Apfel", 0.5)
brot = Artikel("Brot", 1.5)

einkaufsliste = Einkaufsliste()
einkaufsliste.artikel_hinzufuegen(apfel)
einkaufsliste.artikel_hinzufuegen(brot)
print(einkaufsliste.gesamtpreis())
```

#### Code 6: Komposition Beispiel

```python
class Arm:
    def bewegen(self):
        return "Arm bewegt sich"

class Bein:
    def bewegen(self):
        return "Bein bewegt sich"

class Roboter:
    def __init__(self):
        self.arm = Arm()
        self.bein = Bein()

    def bewegen(self):
        return f"{self.arm.bewegen()} und {self.bein.bewegen()}"

# Beispielhafte Nutzung:
roboter = Roboter()
print(roboter.bewegen())
```

## Modul 3: Fortgeschrittene Konzepte der Objektorientierung

### Lab 3.1: Mehrfachvererbung

#### Code 7: Mehrfachvererbung Beispiel

```python
class A:
    def __init__(self):
        print("A init")

    def feature(self):
        print("Feature A")

class B:
    def __init__(self):
        print("B init")

    def feature(self):
        print("Feature B")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

# Beispielhafte Nutzung:
obj = C()
obj.feature()
```

### Lab 3.2: Magic Methods

#### Code 8: Nutzung von Magic Methods

```python
class Zahl:
    def __init__(self, wert):
        self.wert = wert

    def __str__(self):
        return str(self.wert)

    def __mul__(self, andere_zahl):
        return self.wert * andere_zahl.wert

# Beispielhafte Nutzung:
zahl1 = Zahl(3)
zahl2 = Zahl(4)
print(zahl1 * zahl2)
```

### Lab 3.3: Klassenabstraktion

#### Code 9: Abstrakte Klassen Beispiel

```python
from abc import ABC, abstractmethod

class Tier(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Hund(Tier):
    def make_sound(self):
        return "Wuff"

class Katze(Tier):
    def make_sound(self):
        return "Miau"

# Beispielhafte Nutzung:
hund = Hund()
katze = Katze()
print(hund.make_sound())
print(katze.make_sound())
```

## Modul 4: Design Patterns für sauberen Code

### Lab 4.1: Factory Pattern

#### Code 10: Einfaches Factory Pattern Beispiel

```python
class Hund:
    def make_sound(self):
        return "Wuff"

class Katze:
    def make_sound(self):
        return "Miau"

class TierFactory:
    @staticmethod
    def get_tier(tier_typ):
        if tier_typ == "Hund":
            return Hund()
        elif tier_typ == "Katze":
            return Katze()
        else:
            return None

# Beispielhafte Nutzung:
tier = TierFactory.get_tier("Hund")
print(tier.make_sound())
```

### Lab 4.2: Observer Pattern

#### Code 11: Observer Pattern Beispiel

```python
class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        pass

class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Received message: {message}")

# Beispielhafte Nutzung:
subject = Subject()
observer = ConcreteObserver()
subject.add_observer(observer)
subject.notify_observers("Hallo Welt")
```

...
