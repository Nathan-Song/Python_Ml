
# Python Schulung: Vom Code zur Distribution

## Einführung

In dieser Schulung lernen Sie, wie Sie Python-Code von einfachen Skripten zu vollständig verteilbaren Paketen entwickeln können. Wir werden die Konzepte von Modulen, Paketen und der Distribution von Python-Projekten behandeln, einschließlich der Erstellung von `setup.py`-Dateien.

## Module und Pakete

### Module

Ein Python-Modul ist einfach eine `.py` Datei, die Python-Definitionen und -Anweisungen enthält. Ein Modul kann Funktionen, Klassen und Variablen enthalten, die in anderen Modulen oder Skripten wiederverwendet werden können.

```python
# example_module.py
def greet(name):
    return f"Hello, {name}!"
```

### Pakete

Ein Paket ist eine Sammlung von Modulen, die in einem Verzeichnis organisiert sind. Jedes Verzeichnis, das als Paket fungieren soll, muss eine `__init__.py` Datei enthalten, selbst wenn diese leer ist.

```text
my_package/
    __init__.py
    module1.py
    module2.py
```

```python
# module1.py
def add(a, b):
    return a + b
```

```python
# module2.py
def subtract(a, b):
    return a - b
```

### Importieren von Modulen und Paketen

Sie können Funktionen und Klassen aus Modulen und Paketen importieren und verwenden.

```python
from my_package.module1 import add
result = add(2, 3)
print(result)  # Output: 5
```

## Distribution eines Python-Projekts

### `setup.py` Datei

Die `setup.py` Datei ist das Herzstück jedes Python-Pakets. Sie beschreibt das Paket und dessen Metadaten wie Name, Version, Autor und Abhängigkeiten.

```python
from setuptools import setup, find_packages

setup(
    name="mein_paket",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.20.0",
    ],
    author="Ihr Name",
    description="Ein Beispiel-Python-Paket",
)
```

### Erstellung eines verteilbaren Pakets

Um ein verteilbares Paket zu erstellen, verwenden Sie das `setuptools`-Modul. Dies generiert eine `.tar.gz` oder `.whl` Datei, die über PyPI oder privat verteilt werden kann.

```bash
python setup.py sdist bdist_wheel
```

### Installation des Pakets

Einmal erstellt, kann Ihr Paket mit `pip` installiert werden:

```bash
pip install mein_paket-0.1-py3-none-any.whl
```

## Praktische Anwendung

In der Praxis bedeutet das Erstellen von Python-Paketen, dass Sie Ihren Code einfach teilen und wiederverwenden können. Dies ist besonders nützlich in größeren Projekten oder bei der Entwicklung von Tools, die von anderen Entwicklern verwendet werden sollen.

### Beispielprojekt: CLI-Tool für den Wetterbericht

- Modularer Code: Aufteilung der Funktionen in Module (API-Aufrufe, Parsing, Anzeige)
- Paketierung: Bereitstellung als wiederverwendbares Paket
- Distribution: Erstellung eines distributierbaren Pakets für andere Entwickler

## Fazit

Das Verstehen und Verwenden von Modulen, Paketen und Setup-Skripten ist entscheidend für die professionelle Python-Entwicklung. Es ermöglicht nicht nur die Organisation von Code, sondern auch dessen einfache Verteilung und Wiederverwendung in verschiedenen Projekten.
