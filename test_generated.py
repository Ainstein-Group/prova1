```python
import unittest

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