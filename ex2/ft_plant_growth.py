#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = plant_age

    def show(self) -> None:
        print(self.name, ": ", round(self.height, 2), "cm, ",
              self.plant_age, " days old", sep="")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.plant_age += 1


def ft_plant_growth() -> None:
    growth = 0.0
    days = 1
    plant = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    plant.show()
    for days in range(1, 8):
        growth += 0.8
        plant.grow()
        plant.age()
        print("=== Day", days, "===")
        plant.show()
        days = days + 1
    print("Growth this week: ", growth, "cm", sep="")


if __name__ == "__main__":
    ft_plant_growth()
