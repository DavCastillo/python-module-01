class Plant:
    def __init__(self, name: str, height: float, plant_age: int) -> None:
        self.name: str = name
        self.__height: float = height
        self.__plant_age: int = plant_age

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__plant_age

    def set_height(self, height: float) -> None:
        if height < 0:
            print(self.name + ": Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height

    def set_age(self, plant_age: int) -> None:
        if plant_age < 0:
            print(self.name + ": Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__plant_age = plant_age

    def show(self) -> None:
        print(self.name, ": ", round(self.get_height(), 2), "cm, ",
              self.get_age(), " days old", sep="")
        # print(f"{self.name}: {self.height}cm, {self.plant_age} days old")


def ft_garden_security() -> None:
    plant = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")
    print("Plant created: ", end='')
    plant.show()
    plant.set_height(25.0)
    print("\nHeight updated: ", plant.get_height(), "cm", sep='')
    plant.set_age(30)
    print("Age updated:", plant.get_age(), "days\n")
    plant.set_height(-30)
    plant.set_age(-25)
    print("\nCurrent state: ", end='')
    plant.show()


if __name__ == "__main__":
    ft_garden_security()
