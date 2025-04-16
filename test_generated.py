Ecco un esempio di come scrivere test unitari per una funzione Python. Supponiamo di avere una funzione `calculate_area` che calcola l'area di un cerchio:

```python
import unittest

def calculate_area(radius):
    if radius < 0:
        return 0
    return 3.14 * radius ** 2

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

if __name__ == "__main__":
    unittest.main()
```

Questo codice include:
1. Una funzione `calculate_area` che calcola l'area di un cerchio.
2. Quattro test cases diversi:
   - Test con raggio positivo
   - Test con raggio zero
   - Test con raggio negativo
   - Test con raggio floating-point
3. Ogni test utilizza `self.assertEqual` per verificare che il risultato sia corretto.
4. Viene utilizzato il modulo `unittest` per eseguire i test.

Per eseguire i test, salva il codice in un file con estensione `.py` e esegui il file. I test verranno eseguiti automaticamente e vedrai i risultati.