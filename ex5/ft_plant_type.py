class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.__name: str = name
        self.__height: float = height
        self.__age: int = age

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self.get_name() + ": Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(self.get_name() + ": Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = age

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old", sep="")
        # print(f"{self.get_name()}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.set_height(self.__height + 0.8)

    def aging(self) -> None:
        self.set_age(self.__age + 1)


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print("", self.get_name(), "is blooming beautifully!")

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n", " Color: ", self.color, sep="")


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
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n",
              " Trunk diamter: ", self._trunk_diameter, "cm", sep="")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n",
              " Harvest season: ", self._harvest_season,
              "\n Nutritional value: ", self._nutritional_value, sep="")

    def grow(self) -> None:
        self.set_height(self.get_height() + 2.1)
        self._nutritional_value += 1


def ft_plant_type() -> None:
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    print("", flower.get_name(), "has not bloomed yet")
    print("[asking the", flower.get_name(), "to bloom]")
    flower.show()
    flower.bloom()

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
