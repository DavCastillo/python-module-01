#!/usr/bin/env python3

class Plant:

    class Data:
        def __init__(
            self,
            grow_count: int,
            age_count: int,
            show_count: int
        ) -> None:
            self._grow_count = grow_count
            self._age_count = age_count
            self._show_count = show_count

        def add_grow(self) -> None:
            self._grow_count += 1

        def add_age(self) -> None:
            self._age_count += 1

        def add_show(self) -> None:
            self._show_count += 1

        def get_grow_count(self) -> int:
            return self._grow_count

        def get_age_count(self) -> int:
            return self._age_count

        def get_show_count(self) -> int:
            return self._show_count

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
        self._data = Plant.Data(0, 0, 0)

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

    def get_data(self) -> Data:
        return self._data

    def get_extra_data(self) -> int:
        return 0

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old", sep="")
        self.get_data().add_show()
        # print(f"{self.get_name()}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.set_height(self._height + 0.8)
        self.get_data().add_grow()

    def aging(self) -> None:
        self.set_age(self._age + 1)
        self.get_data().add_age()

    @classmethod
    def create_anon_plant(cls) -> "Plant":
        return cls("Unknown plant", 1.0, 1)

    @staticmethod
    def check_age(age: int) -> None:
        if age < 365:
            print("Is", age, "days more than a year? -> False")
        else:
            print("Is", age, "days more than a year? -> True")


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
            print("", self.get_name(), "is blooming beautifully!")
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
        self._shade_calls = 0

    def produce_shade(self) -> None:
        print("Tree ", self.get_name(), " now produces a shade of ",
              self.get_height(), "cm long and ",
              self._trunk_diameter, "cm wide.", sep='')
        self._shade_calls += 1

    def get_extra_data(self) -> int:
        return self._shade_calls

    def show(self) -> None:
        super().show()
        print(" Trunk diamter: ", self._trunk_diameter, "cm", sep="")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds = 0

    def show(self) -> None:
        super().show()
        print(" Seeds:", self._seeds)

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42


def show_statistics(plant: Plant) -> None:
    print("[statistics for ", plant.get_name(), "]", sep='')
    print("Stats: ", plant.get_data().get_grow_count(), " grow, ",
          plant.get_data().get_age_count(), " age, ",
          plant.get_data().get_show_count(), " show", sep="", end="")
    if plant.__class__.__name__ == "Tree":
        print("\n", plant.get_extra_data(), "shade")
    else:
        print()


def ft_garden_analytics() -> None:
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    anon = Plant.create_anon_plant()

    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    Plant.check_age(30)
    Plant.check_age(400)

    print("\n=== Flower")
    flower.show()
    show_statistics(flower)
    print("[asking the", flower.get_name(), "to grow and bloom]")
    flower.bloom()
    flower.grow()
    flower.show()
    show_statistics(flower)

    print("\n=== Tree")
    tree.show()
    show_statistics(tree)
    print("[asking the", tree.get_name(), "to produce shade]")
    tree.produce_shade()
    show_statistics(tree)

    print("\n=== Seed")
    seed.show()
    print("[make", seed.get_name(), "grow, age and bloom]")
    seed.grow()
    seed.aging()
    seed.bloom()
    seed.show()
    show_statistics(seed)

    print("\n=== Anonymous")
    anon.show()
    show_statistics(anon)


if __name__ == "__main__":
    ft_garden_analytics()
