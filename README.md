```markdown
# Calcola l'area di un triangolo

Questo codice fornisce una funzione per calcolare l'area di un triangolo e un test unitario per verificare il suo funzionamento.

## Funzione `calcola_area_triangolo`

```python
def calcola_area_triangolo(base, altezza):
  """
  Questa funzione calcola l'area di un triangolo.

  Args:
    base: La lunghezza della base del triangolo.
    altezza: L'altezza del triangolo rispetto alla base.

  Returns:
    L'area del triangolo.
  """
  area = 0.5 * base * altezza
  return area
```

La funzione `calcola_area_triangolo` accetta due argomenti: `base` (la lunghezza della base del triangolo) e `altezza` (l'altezza del triangolo rispetto alla base). 

Calcola l'area del triangolo usando la formula: `area = 0.5 * base * altezza`.

## Esempi di utilizzo

Il codice include due esempi di utilizzo della funzione:

```python
base1 = 10
altezza1 = 5
area1 = calcola_area_triangolo(base1, altezza1)
print(f"L'area del triangolo con base {base1} e altezza {altezza1} è: {area1}")

base2 = 7
altezza2 = 12
area2 = calcola_area_triangolo(base2, altezza2)
print(f"L'area del triangolo con base {base2} e altezza {altezza2} è: {area2}")
```

Questi esempi calcolano l'area di due triangoli con parametri specifici e stampano il risultato a schermo.

## Test unitari

Il codice include un test unitario per verificare il corretto funzionamento della funzione `calcola_area_triangolo`:

```python
import unittest

class TestCalcolaAreaTriangolo(unittest.TestCase):

    def test_base_e_altezza_positivi(self):
        self.assertEqual(calcola_area_triangolo(10, 5), 25)

    def test_base_e_altezza_zero(self):
        self.assertEqual(calcola_area_triangolo(0, 5), 0)

    def test_base_negativo(self):
        with self.assertRaises(ValueError):
            calcola_area_triangolo(-10, 5)

    def test_altezza_negativa(self):
        with self.assertRaises(ValueError):
            calcola_area_triangolo(10, -5)

if __name__ == '__main__':
    unittest.main()  
```

Il test utilizza la libreria `unittest` per verificare che la funzione restituisca il risultato corretto in diversi scenari, tra cui:

* Base e altezza positivi
* Base o altezza zero
* Base o altezza negativo (generando un ValueError)