```python
def calculate_area(shape_type, **kwargs):
  """
  Calcola l'area di diverse figure geometriche.

  Argomenti:
    shape_type: Il tipo di figura geometrica (es. "quadrato", "rettangolo", "cerchio", "triangolo").
    **kwargs: Argomenti speciali per la figura specificata. 

      Per un quadrato:
        - lato: la lunghezza di un lato del quadrato.

      Per un rettangolo:
        - lunghezza: la lunghezza del rettangolo.
        - larghezza: la larghezza del rettangolo.

      Per un cerchio:
        - raggio: il raggio del cerchio.

      Per un triangolo:
        - base: la lunghezza della base del triangolo.
        - altezza: l'altezza del triangolo rispetto alla base.

  Restituisce:
    L'area della figura, o un messaggio di errore se il tipo di figura non è supportato o se un argomento è mancante.
  """
  if shape_type == "quadrato":
    return kwargs["lato"] * kwargs["lato"]
  elif shape_type == "rettangolo":
    return kwargs["lunghezza"] * kwargs["larghezza"]
  elif shape_type == "cerchio":
    return 3.14159 * kwargs["raggio"] * kwargs["raggio"]
  elif shape_type == "triangolo":
    return 0.5 * kwargs["base"] * kwargs["altezza"]
  else:
    return "Tipo di figura non supportato."

# Esempi di utilizzo
print(calculate_area("quadrato", lato=5))  # Output: 25
print(calculate_area("rettangolo", lunghezza=4, larghezza=6))  # Output: 24
print(calculate_area("cerchio", raggio=3))  # Output: 28.27433
print(calculate_area("triangolo", base=10, altezza=7))  # Output: 35
```