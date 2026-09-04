class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name: str = name
        self.height: float = height
        self.plant_age: int = plant_age

    def show(self) -> None:
        print(self.name, ": ", round(self.height, 2), "cm, ",
              self.plant_age, " days old", sep="")
        # print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self) -> None:
        self.height = self.height + 0.8

    def age(self) -> None:
        self.plant_age += 1


def ft_plant_factory() -> None:
    plant1 = Plant("Rose", 25.0, 30)
    plant2 = Plant("Oak", 200.0, 365)
    plant3 = Plant("Cactus", 5.0, 90)
    plant4 = Plant("Sunflower", 80.0, 45)
    plant5 = Plant("Fern", 15.0, 120)
    plants = (plant1, plant2, plant3, plant4, plant5)
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created:", end=' ')
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
