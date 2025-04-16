```python
# Scrivi una funzione che calcola l'area di un triangolo.

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

# Esempi di utilizzo
base1 = 10
altezza1 = 5
area1 = calcola_area_triangolo(base1, altezza1)
print(f"L'area del triangolo con base {base1} e altezza {altezza1} è: {area1}")

base2 = 7
altezza2 = 12
area2 = calcola_area_triangolo(base2, altezza2)
print(f"L'area del triangolo con base {base2} e altezza {altezza2} è: {area2}") 
```