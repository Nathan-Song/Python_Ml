
# Python Schulung: Simulation und Modellierung – Komplexe Systeme parallel simulieren

## Einleitung

In dieser Schulung beschäftigen wir uns mit der Simulation und Modellierung komplexer Systeme unter Verwendung von Python. Insbesondere legen wir den Fokus auf die parallele Simulation, um die Effizienz und Leistung bei der Modellierung großer und komplexer Systeme zu steigern.

## Was ist Simulation und Modellierung?

Simulation und Modellierung sind Techniken, die verwendet werden, um reale Systeme durch mathematische Modelle nachzubilden. Diese Techniken sind in vielen Disziplinen wie Physik, Biologie, Wirtschaft und Ingenieurwesen weit verbreitet. Ziel ist es, das Verhalten eines Systems zu verstehen und Vorhersagen über dessen zukünftige Entwicklung zu treffen.

## Parallele Simulation

Parallelisierung ist der Prozess, bei dem eine Aufgabe in kleinere Teile zerlegt wird, die gleichzeitig (parallel) ausgeführt werden können. Bei der Simulation komplexer Systeme kann die Parallelisierung die Verarbeitungszeit erheblich verkürzen.

### Beispiel: Parallele Simulation eines Zellulären Automaten

Ein zellulärer Automat besteht aus einem Gitter von Zellen, die sich in einer von mehreren Zuständen befinden können. Der Zustand jeder Zelle wird basierend auf den Zuständen ihrer Nachbarzellen aktualisiert. Diese Berechnungen können parallel durchgeführt werden, da der Zustand einer Zelle unabhängig von anderen Zellen berechnet werden kann.

```python
import numpy as np
from multiprocessing import Pool

def update_cell(state, x, y):
    # Beispielhafte Regel: Zustand der Zelle bleibt unverändert
    return state[x, y]

def simulate_step(state):
    new_state = np.zeros_like(state)
    with Pool() as pool:
        results = [pool.apply_async(update_cell, args=(state, x, y)) for x in range(state.shape[0]) for y in range(state.shape[1])]
        for i, res in enumerate(results):
            x, y = divmod(i, state.shape[1])
            new_state[x, y] = res.get()
    return new_state

# Beispielinitialisierung
state = np.random.randint(2, size=(10, 10))
new_state = simulate_step(state)
```

## Werkzeuge und Bibliotheken

### Multiprocessing

Das `multiprocessing`-Modul in Python ermöglicht das Erstellen von parallelen Prozessen, was insbesondere bei CPU-intensiven Aufgaben nützlich ist.

### NumPy

`NumPy` ist eine grundlegende Bibliothek für wissenschaftliches Rechnen in Python. Sie bietet Unterstützung für große, mehrdimensionale Arrays und Matrizen sowie eine Sammlung mathematischer Funktionen.

### Parallel Processing mit `dask`

`Dask` ist eine flexible Parallel-Computing-Bibliothek für analytische Workloads, die entwickelt wurde, um `NumPy`, `pandas`, und `scikit-learn` zu ergänzen. `Dask` ermöglicht es, große Aufgaben effizient zu verteilen und auf verschiedenen Kernen oder sogar Maschinen auszuführen.

## Praktische Anwendung

Die Konzepte der parallelen Simulation und Modellierung lassen sich in vielen Bereichen anwenden, wie z.B.:

- **Finanzmodelle:** Parallelisierung von Monte-Carlo-Simulationen zur Risikobewertung.
- **Physikalische Systeme:** Simulation von Partikelsystemen oder Klimamodellen.
- **Biologische Systeme:** Modellierung der Ausbreitung von Krankheiten in Populationen.

### Beispielprojekt: Parallele Monte-Carlo-Simulation

Monte-Carlo-Simulationen sind weit verbreitete Methoden zur Schätzung mathematischer Funktionen und zur Lösung komplexer Probleme durch zufällige Stichproben. Durch Parallelisierung können Tausende von Simulationen gleichzeitig ausgeführt werden, was die Effizienz drastisch erhöht.

```python
import numpy as np
from multiprocessing import Pool

def monte_carlo_simulation(n):
    count = 0
    for _ in range(n):
        x, y = np.random.rand(2)
        if x**2 + y**2 <= 1:
            count += 1
    return count

def parallel_monte_carlo(total_points, workers=4):
    points_per_worker = total_points // workers
    with Pool(workers) as pool:
        results = pool.map(monte_carlo_simulation, [points_per_worker] * workers)
    return 4 * sum(results) / total_points

# Beispiel für 1 Million Punkte mit 4 Workern
pi_estimate = parallel_monte_carlo(10**6, workers=4)
print(f"Pi estimate: {pi_estimate}")
```

## Fazit

Die parallele Simulation und Modellierung komplexer Systeme ist eine leistungsfähige Methode, um die Rechenzeiten erheblich zu verkürzen und somit größere und genauere Modelle zu erstellen. Durch den Einsatz von Python und seinen leistungsstarken Bibliotheken können diese Techniken effektiv implementiert werden.

