class Animal:
    def __init__(self) -> None:
        self.number_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")

carp = Fish()

carp.breathe()