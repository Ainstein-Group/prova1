```python
from typing import List

class Vase:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.water = 0

    def fill(self) -> None:
        self.water = self.capacity

    def empty(self) -> None:
        self.water = 0

    def transfer(self, amount: int) -> None:
        if amount > self.water:
            raise ValueError("Not enough water in the vase")
        self.water -= amount

    def get_water(self) -> int:
        return self.water

class WaterMeasurer:
    def __init__(self):
        self.vase5 = Vase(5)
        self.vase3 = Vase(3)

    def measure(self) -> List[str]:
        self.vase5.fill()
        operations = []
        while self.vase5.water > 4:
            if self.vase5.water > 3:
                self.vase3.transfer(3)
                operations.append(f"Transfer 3 liters from vase 5 to vase 3")
            self.vase5.transfer(2)
            operations.append(f"Transfer 2 liters from vase 5 to vase 3")
        return operations

if __name__ == "__main__":
    measurer = WaterMeasurer()
    operations = measurer.measure()
    print("Operations:")
    for operation in operations:
        print(operation)
    print(f"Final water level in vase 3: {measurer.vase3.get_water()} liters")
    print(f"Final water level in vase 5: {measurer.vase5.get_water()} liters")
```