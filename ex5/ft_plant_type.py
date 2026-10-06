#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height > 0.0:
            self._height = height
        else:
            self._height = 1.0
            print(self._name + ": Error, height can't be negative")
            print("Height set to 1.0")
        if age > 0:
            self._age = age
        else:
            self._age = 1
            print(self._name + ": Error, age can't be negative")
            print("Age set to 1")

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self.get_name() + ": Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(self.get_name() + ": Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old", sep="")

    def grow(self) -> None:
        self.set_height(self._height + 0.8)

    def aging(self) -> None:
        self.set_age(self._age + 1)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_bloomed = False

    def bloom(self) -> None:
        self._is_bloomed = True

    def show(self) -> None:
        super().show()
        print(" Color:", self._color)
        if self._is_bloomed:
            print("", self.get_name(), "is blooming beatifully!")
        else:
            print("", self.get_name(), "has not bloomed yet")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float,
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("Tree ", self.get_name(), " now produces a shade of ",
              self.get_height(), "cm long and ",
              self._trunk_diameter, "cm wide.", sep='')

    def show(self) -> None:
        super().show()
        print(" Trunk diamter: ", self._trunk_diameter, "cm", sep="")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,

    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(" Harvest season:", self._harvest_season)
        print(" Nutritional value:", self._nutritional_value)

    def grow(self) -> None:
        self.set_height(self.get_height() + 2.1)
        self._nutritional_value += 1


def ft_plant_type() -> None:
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable = Vegetable("Tomato", 5.0, 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    print("[asking the", flower.get_name(), "to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree")
    tree.show()
    print("[asking the", tree.get_name(), "to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable")
    vegetable.show()
    print("[make", vegetable.get_name(), "grow and age for 20 days]")
    for _ in range(20):
        vegetable.grow()
        vegetable.aging()
    vegetable.show()


if __name__ == "__main__":
    ft_plant_type()
