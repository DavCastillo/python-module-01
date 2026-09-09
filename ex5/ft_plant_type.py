class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.__height: float = height
        self.__age: int = age

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self.name + ": Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(self.name + ": Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = age

    def show(self) -> None:
        print(self.name, ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old", sep="")
        # print(f"{self.name}: {self.height}cm, {self.age} days old")


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
        print("", self.name, "is blooming beautifully!")
    
    def show(self) -> None:
        print(self.name, ": ", round(self.get_height(), 2), "cm, ",
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
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print("Tree ", self.name, " now produces a shade of ",
              self.get_height(), "cm long and ", self.trunk_diameter, " wide.",
              sep='')

    def show(self) -> None:
        print(self.name, ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n",
              " Trunk diamter: ", self.trunk_diameter, "cm", sep="")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str
    ) -> None:
        super().__init__(name, height, age)
        self.__color = color


def ft_plant_type() -> None:
    flower = Flower("Rose", 15.0, 10, "red")
    tree = Tree("Oak", 200.0, 365, 5.0)
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    print("", flower.name, "has not bloomed yet")
    print("[asking the", flower.name, "to bloom]")
    flower.show()
    flower.bloom()
    print("\n=== Tree")
    tree.show()
    print("[asking the", tree.name, "to produce shade]")
    tree.produce_shade()



if __name__ == "__main__":
    ft_plant_type()
