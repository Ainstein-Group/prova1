```markdown
# Tic Tac Toe

## Descrizione

Questo progetto implementa un gioco di Tic Tac Toe in Python con due agenti che possono giocare contro se stessi o contro un giocatore umano. Il gioco può essere giocato su una griglia di dimensioni variabili.

## Requisiti e Dipendenze

* Python 3.6 o superiore
* pytest (per i test)

## Guida all'installazione

1.  Clone o scarica il repository.
2.  Apri un terminale e naviga nella directory del progetto.
3.  Esegui il comando `pip install -r requirements.txt` per installare le dipendenze.

## Guida all'utilizzo

Per giocare al Tic Tac Toe, puoi eseguire il file `main.py`. Il gioco inizierà con due agenti casuali. Puoi modificare il nome e la strategia degli agenti nel file `main.py`.

**Esempio di gioco:**

```
Agent 1:  Test Agent (random)
Agent 2:  Test Agent (random)

     0 0 0
     0 0 0
     0 0 0
     
     1 0 0
     0 0 0
     0 0 0
     
     0 1 0
     0 0 0
     0 0 0
     
Test Agent wins!
```

**Strategie disponibili:**

*   `random`: L'agente sceglie una mossa casuale.
*   `minimax`: L'agente utilizza l'algoritmo minimax per scegliere la mossa migliore. (Da implementare)

## Architettura

Il gioco è composto da tre classi principali:

*   **Board:** Rappresenta la griglia di gioco.
*   **Agent:** Rappresenta un agente che gioca al Tic Tac Toe.
*   **Game:** Gestisce il flusso di gioco e le interazioni tra gli agenti.

## API Reference

**Board:**

| Metodo | Descrizione |
|---|---|
| `__init__(self, size)` | Inizializza la griglia di gioco con la dimensione specificata. |
| `print_board(self)` | Stampa la griglia di gioco a schermo. |

**Agent:**

| Attributo | Descrizione |
|---|---|
| `name` | Il nome dell'agente. |
| `strategy` | La strategia di gioco dell'agente. |
| `score` | Il punteggio dell'agente. |

| Metodo | Descrizione |
|---|---|
| `__init__(self, name, strategy)` | Inizializza l'agente con il nome e la strategia specificati. |
| `make_move(self, board)` | Fa una mossa nel gioco in base alla strategia dell'agente. |

**Game:**

| Attributo | Descrizione |
|---|---|
| `board` | L'istanza della classe `Board`. |
| `agent1` | L'istanza della classe `Agent` per il primo giocatore. |
| `agent2` | L'istanza della classe `Agent` per il secondo giocatore. |
| `current_turn` | Il numero del giocatore corrente. |

| Metodo | Descrizione |
|---|---|
| `__init__(self, board_size, agent1, agent2)` | Inizializza il gioco con la dimensione della griglia e gli agenti. |
| `start_game(self)` | Avvia il gioco e gestisce il flusso di gioco. |
| `check_win(self)` | Controlla se un giocatore ha vinto la partita. |

## Guida ai test

Per eseguire i test, usa il comando `pytest`.

## Contribuzione e Licenza

Questo progetto è open-source e licenziato sotto la licenza MIT.

Contribuisci al progetto inviando pull request con i tuoi miglioramenti e correzioni.

```