
# Python Schulung: Fehler finden und beheben durch Debugging und Logging

## Einleitung

In dieser Schulung lernen Sie, wie Sie effektiv Fehler in Python-Anwendungen finden und beheben können. Der Fokus liegt dabei auf den Techniken des Debuggings und der Nutzung von Logging, um Laufzeitfehler zu diagnostizieren und zu beheben.

## Debugging in Python

### Verwendung von `print` zum Debugging

Die einfachste Form des Debuggings ist die Ausgabe von Variablenwerten und Zuständen mittels `print`.

```python
def divide(a, b):
    print(f"a: {a}, b: {b}")  # Debug-Ausgabe
    return a / b

result = divide(4, 2)
print(f"Result: {result}")
```

### Einsatz des Debuggers `pdb`

`pdb` ist der Python-Debugger, mit dem Sie Schritt für Schritt durch Ihren Code gehen, Variablen inspizieren und den Codefluss nachvollziehen können.

```python
import pdb

def divide(a, b):
    pdb.set_trace()  # Startet den Debugger
    return a / b

result = divide(4, 2)
```

### Fehlerbehandlung mit `try-except`

Fehler können abgefangen und behandelt werden, um Abstürze der Anwendung zu verhindern.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Fehler: {e}")
        return None

result = divide(4, 0)
print(f"Result: {result}")
```

## Logging in Python

### Einführung in das Logging-Modul

Das Logging-Modul ermöglicht die Protokollierung von Informationen während der Laufzeit, die später zur Diagnose von Problemen verwendet werden können.

```python
import logging

logging.basicConfig(level=logging.INFO)

def divide(a, b):
    logging.info(f"Teilen {a} durch {b}")
    return a / b

result = divide(4, 2)
logging.info(f"Resultat: {result}")
```

### Verschiedene Logging-Ebenen

Das Logging-Modul unterstützt verschiedene Ebenen, um die Relevanz der Nachrichten zu kennzeichnen:

- `DEBUG`: Detaillierte Informationen, typischerweise nur zur Diagnose.
- `INFO`: Bestätigungsnachrichten, dass Dinge wie erwartet funktionieren.
- `WARNING`: Ein Hinweis, dass etwas Unerwartetes passiert ist oder in naher Zukunft passieren könnte.
- `ERROR`: Ein schwerwiegendes Problem, das das Programm jedoch nicht stoppt.
- `CRITICAL`: Ein sehr schwerwiegendes Problem, das das Programm möglicherweise stoppen wird.

```python
logging.debug("Dies ist eine Debug-Nachricht")
logging.info("Dies ist eine Info-Nachricht")
logging.warning("Dies ist eine Warnung")
logging.error("Dies ist eine Fehlermeldung")
logging.critical("Dies ist eine kritische Fehlermeldung")
```

## Praktische Anwendung

In dieser Schulung werden Sie lernen, wie Sie durch den gezielten Einsatz von Debugging und Logging komplexe Probleme in Python-Anwendungen identifizieren und beheben können. Dies wird durch praktische Übungen und Projekte unterstützt, wie z.B. die Analyse einer fehlerhaften Datenverarbeitungs-Pipeline.

### Beispielprojekt: Datenverarbeitungs-Pipeline

- Debuggen von fehlerhaften Datenverarbeitungsprozessen
- Logging der Zwischenschritte zur besseren Nachvollziehbarkeit
- Identifikation und Behebung von häufigen Fehlern wie Nullpointer-Ausnahmen und fehlerhaften Datenformaten

## Fazit

Debugging und Logging sind wesentliche Fähigkeiten für jeden Python-Entwickler. Durch das Verständnis und den effektiven Einsatz dieser Techniken können Sie Fehler schneller finden und Ihre Anwendungen robuster machen.
