
# Python Schulung: Grundlagen der Objektorientierung

## Einführung

Die Objektorientierung ist ein Programmierparadigma, das auf Konzepten wie Klassen, Objekten, Vererbung, Polymorphismus und Kapselung basiert. Python bietet als eine objektorientierte Sprache die Möglichkeit, komplexe Softwareanwendungen effizient zu gestalten.

## Grundkonzepte der Objektorientierung in Python

### Klassen und Objekte

Klassen sind Baupläne für Objekte und definieren Attribute und Methoden, die von Objekten genutzt werden können.

```python
class Auto:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def zeige_details(self):
        print(f"Marke: {self.marke}, Modell: {self.modell}")

mein_auto = Auto("Toyota", "Corolla")
mein_auto.zeige_details()
```

### Vererbung

Vererbung ermöglicht das Erstellen neuer Klassen auf der Basis bestehender Klassen, wobei Eigenschaften und Verhaltensweisen übernommen werden.

```python
class Elektroauto(Auto):
    def __init__(self, marke, modell, batteriekapazitaet):
        super().__init__(marke, modell)
        self.batteriekapazitaet = batteriekapazitaet

    def zeige_details(self):
        super().zeige_details()
        print(f"Batteriekapazität: {self.batteriekapazitaet} kWh")

mein_elektroauto = Elektroauto("Tesla", "Model S", 85)
mein_elektroauto.zeige_details()
```

### Polymorphismus und Methodenüberladung

Polymorphismus in Python ermöglicht es, dass Methoden unterschiedliche Formen annehmen können, abhängig davon, welche Objekte sie aufrufen.

```python
def zeige_info(fahrzeug):
    fahrzeug.zeige_details()

zeige_info(mein_auto)
zeige_info(mein_elektroauto)
```

### Kapselung

Kapselung bezieht sich auf die Einschränkung des Zugriffs auf Methoden und Attribute, um das Innere eines Objekts zu schützen.

```python
class GeschuetztesAuto(Auto):
    def __init__(self, marke, modell, geheimcode):
        super().__init__(marke, modell)
        self.__geheimcode = geheimcode  # Privates Attribut

    def zeige_geheimcode(self, code):
        if code == self.__geheimcode:
            print(f"Geheimcode: {self.__geheimcode}")
        else:
            print("Falscher Code!")

mein_geschuetztes_auto = GeschuetztesAuto("Ford", "Mustang", 1234)
mein_geschuetztes_auto.zeige_geheimcode(1234)
```

## Fazit

Die Objektorientierung in Python bietet eine robuste Basis für die Entwicklung modularer und wiederverwendbarer Software. Durch das Verstehen dieser Prinzipien können Entwickler ihre Anwendungen effizient und effektiv gestalten.
