```markdown
# Calcola l'area di un cerchio

Questo progetto contiene un codice python che implementa la funzione `calculate_area` per calcolare l'area di un cerchio dato il suo raggio. Il codice include anche un modulo di test unitaria per testare la funzione `calculate_area`.

## `calculate_area`

La funzione `calculate_area` prende un valore float `radius` come input e restituisce l'area del cerchio corrispondente. Se il raggio è negativo, la funzione restituisce 0.

```python
def calculate_area(radius):
    if radius < 0:
        return 0
    return 3.14 * radius ** 2
```

## Test unitaria

Il modulo di test unitario implementa quattro test cases per valutare la funzione `calculate_area`:

- Test con raggio positivo
- Test con raggio zero
- Test con raggio negativo
- Test con raggio floating-point

Ogni test utilizza `self.assertEqual` per verificare che il valore restituito dalla funzione corrisponda all'area attesa.

```python
import unittest

class TestCalculateArea(unittest.TestCase):
    
    def test_positive_radius(self):
        radius = 5
        expected_area = 3.14 * (radius ** 2)
        self.assertEqual(calculate_area(radius), expected_area)
    
    def test_zero_radius(self):
        radius = 0
        expected_area = 0
        self.assertEqual(calculate_area(radius), expected_area)
    
    def test_negative_radius(self):
        radius = -3
        expected_area = 0
        self.assertEqual(calculate_area(radius), expected_area)
    
    def test_float_radius(self):
        radius = 2.5
        expected_area = 3.14 * (radius ** 2)
        self.assertEqual(calculate_area(radius), expected_area)
```

## Come eseguire i test

Per eseguire i test, salva il codice in un file python (ad esempio `calculate_area.py`) ed esegui il seguente comando da terminale:

```bash
python calculate_area.py
```

Il modulo `unittest` eseguirà i test e mostrerà i risultati.