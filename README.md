```markdown
# Labirinto: Un algoritmo A* per la ricerca di percorsi

## Descrizione

Questo progetto implementa l'algoritmo A* per trovare il percorso più breve tra due punti in un labirinto rappresentato da una matrice bidimensionale. L'algoritmo è stato implementato in Python e utilizza una struttura dati heap per gestire la priorità delle celle da esplorare.

## Requisiti e Dipendenze

* Python 3.6 o superiore
* `heapq` (modulo standard Python)
* `logging` (modulo standard Python)

## Guida all'installazione

1. Clone il repository: `git clone https://github.com/your-username/labirinto.git`
2. Installa le dipendenze: `pip install -r requirements.txt`

## Guida all'utilizzo

Per utilizzare il progetto, è possibile eseguire il file `main.py`. Il codice definisce un labirinto predefinito, un punto di partenza e un punto di arrivo. L'algoritmo A* viene quindi utilizzato per trovare il percorso tra questi due punti.

```python
import logging

# Configura il livello di log
logging.basicConfig(level=logging.INFO)

# Definisci il labirinto
grid = [
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 0]
]
start = (0, 0)
goal = (2, 2)

# Crea un'istanza della classe Labirinto
labirinto = Labirinto(grid, start, goal)

# Esegui l'algoritmo A*
path = labirinto.astar()

# Stampa il percorso trovato
logging.info("Percorso trovato: %s", path)

```

**Esempio di output:**

```
Inizia ricerca percorso...
Percorso trovato: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
```

## Architettura e Componenti

Il progetto è strutturato in un unico file Python, `labirinto.py`. La classe principale `Labirinto` gestisce l'algoritmo A* e la rappresentazione del labirinto. 

**Componenti principali:**

* **Classe `Labirinto`:**
    * `__init__(self, grid, start, goal)`: Inizializza il labirinto con la matrice `grid`, il punto di partenza `start` e il punto di arrivo `goal`.
    * `heuristic(self, a, b)`: Calcola la distanza euristica tra due punti.
    * `astar(self)`: Esegue l'algoritmo A* per trovare il percorso.
    * `__str__(self)`: Restituisce una rappresentazione stringa del labirinto.

## API Reference

**Classe `Labirinto`:**

* **`__init__(self, grid, start, goal)`:**

    * `grid`: Matrice bidimensionale che rappresenta il labirinto, dove 0 indica una cella percorribile e 1 indica un ostacolo.
    * `start`: Tuple che rappresenta le coordinate del punto di partenza.
    * `goal`: Tuple che rappresenta le coordinate del punto di arrivo.

* **`heuristic(self, a, b)`:**

    * Calcola la distanza euristica tra due punti `a` e `b` utilizzando la distanza Manhattan.

* **`astar(self)`:**

    * Esegue l'algoritmo A* per trovare il percorso tra il punto di partenza e il punto di arrivo. Restituisce una lista di tuple che rappresentano le coordinate del percorso, oppure la stringa "Nessun percorso possibile" se non esiste un percorso.

* **`__str__(self)`:**

    * Restituisce una rappresentazione stringa del labirinto.

## Guida ai Test

Il progetto include un test unitario con pytest per verificare il corretto funzionamento dell'algoritmo A* e delle sue funzioni. 

Per eseguire i test, è possibile utilizzare il comando `pytest`.

## Contribuisci

Questo progetto è open-source e benvenuto ogni contributo.

Per contribuire, è possibile:

* Richiedere nuove funzionalità
* Rilevare e segnalare bug
* Migliorare la documentazione




## Licenza

Questo progetto è rilasciato sotto la licenza MIT.



```