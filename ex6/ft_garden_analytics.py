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

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_data(self) -> Data:
        return self._data

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
    def create_anon_plant(cls, height: float, age: int) -> "Plant":
        return cls("Unknown plant", height, age)

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
        color: str,
        bloom_status: str
    ) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom_status = self._name + bloom_status

    def bloom(self) -> None:
        self._bloom_status = self.get_name() + "is blooming beautifully"

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n", " Color: ", self._color,
              "\n ", self._bloom_status, sep="")
        self.get_data().add_show()



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

    def get_shade_calls(self) -> int:
        return self._shade_calls

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n",
              " Trunk diamter: ", self._trunk_diameter, "cm", sep="")
        self.get_data().add_show()


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
        self.get_data().add_show()

    def grow(self) -> None:
        super().grow()
        self.set_height(self.get_height() + 1.3)
        self._nutritional_value += 1


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        bloom_status: str,
        seeds: int,
    ) -> None:
        super().__init__(name, height, age, color, bloom_status)
        self._seeds = seeds

    def show(self) -> None:
        print(self.get_name(), ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old\n", " Color: ", self._color,
              "\n ", self._bloom_status, " Seeds: ", self._seeds, sep="")
        self.get_data().add_show()

    def bloom(self):
        super().bloom()
        self._seeds = 42


def show_statistics(plant: Plant | Tree) -> None:
    print("Stats: ", plant.get_data().get_grow_count(), " grow, ",
          plant.get_data().get_age_count(), " age, ",
          plant.get_data().get_show_count(), " show", sep="")
    if plant != Tree:
        print("hey")
    else:
        print(plant.get_shade_calls(), "shade")

def ft_garden_analytics() -> None:
    flower: Flower = Flower("Rose", 15.0, 10, "red", "has not bloomed yet")
    tree: Tree = Tree("Oak", 200.0, 365, 5.0)
    vegetable: Vegetable = Vegetable("Tomato", 5.0, 10, "April", 0)

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
    show_statistics(tree)

    print("\n=== Vegetable")
    vegetable.show()
    print("[make", vegetable.get_name(), "grow and age for 20 days]")
    vegetable.grow()
    vegetable.aging()
    vegetable.show()

    show_statistics(flower)


if __name__ == "__main__":
    ft_garden_analytics()
