
# Python Schulung: Protokollierung und Nachvollziehbarkeit von Programmabläufen

## Einführung in die Protokollierung

Protokollierung (Logging) ist ein wesentlicher Bestandteil der Softwareentwicklung, insbesondere bei der Fehlersuche und -behebung. Durch die Protokollierung können Entwickler den Ablauf eines Programms nachvollziehen und wichtige Informationen über den Zustand des Systems erhalten.

## Grundlegende Protokollierung mit dem `logging` Modul

Das `logging` Modul in Python bietet eine flexible Möglichkeit, Ereignisse während der Ausführung eines Programms aufzuzeichnen. Es ermöglicht das Erfassen von Meldungen auf unterschiedlichen Schweregraden (Debug, Info, Warning, Error, Critical).

### Beispiel für einfache Protokollierung

```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Dies ist eine Informationsmeldung")
logging.warning("Dies ist eine Warnmeldung")
logging.error("Dies ist eine Fehlermeldung")
```

In diesem Beispiel wird die Grundkonfiguration von `logging` verwendet, um Meldungen auf der Konsole auszugeben.

## Protokollierung in Dateien

Neben der Konsolenausgabe können Protokolle auch in Dateien gespeichert werden. Dies ist besonders nützlich, um längerfristige Aufzeichnungen zu erstellen, die zu einem späteren Zeitpunkt analysiert werden können.

### Beispiel: Protokollierung in einer Datei

```python
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Dies ist eine Debug-Meldung")
logging.info("Dies ist eine Info-Meldung")
logging.error("Dies ist eine Fehlermeldung")
```

In diesem Beispiel werden alle Protokollmeldungen in die Datei `app.log` geschrieben, wobei jedes Protokoll den Zeitstempel, das Schweregrad und die Nachricht enthält.

## Log-Level und Filter

Das `logging` Modul bietet verschiedene Log-Level, die es ermöglichen, nur bestimmte Arten von Meldungen aufzuzeichnen. Die gängigsten Log-Level sind:

- `DEBUG`: Detaillierte Informationen, die für die Fehlersuche nützlich sind.
- `INFO`: Bestätigende Nachrichten, die den normalen Ablauf eines Programms anzeigen.
- `WARNING`: Eine Warnung, dass etwas Unerwartetes passiert ist.
- `ERROR`: Ein Fehler ist aufgetreten.
- `CRITICAL`: Ein schwerwiegender Fehler, der das Programm möglicherweise zum Absturz bringt.

### Beispiel: Verwenden von Log-Leveln

```python
import logging

logging.basicConfig(level=logging.WARNING)

logging.debug("Diese Nachricht wird nicht protokolliert")
logging.info("Diese Nachricht wird nicht protokolliert")
logging.warning("Dies ist eine Warnmeldung")
logging.error("Dies ist eine Fehlermeldung")
```

## Praktische Anwendung

Die praktische Anwendung der Protokollierung umfasst die Erstellung von Protokollierungsstrategien, um den Ablauf von Programmen in verschiedenen Umgebungen (Entwicklung, Test, Produktion) nachvollziehbar zu machen.

### Beispielprojekt: Fehlerbehebung in einer Webanwendung

- Protokollierung von Benutzeraktionen
- Erfassung von Fehlern und Ausnahmen
- Überwachung von Systemressourcen und -leistung

## Fazit

Die Protokollierung in Python ist ein leistungsfähiges Werkzeug, um die Nachvollziehbarkeit von Programmabläufen sicherzustellen. Sie hilft Entwicklern, Probleme schneller zu identifizieren und zu beheben, was die Qualität der Software insgesamt verbessert.
