from abc import ABC, abstractmethod


class Tier(ABC):
    @abstractmethod
    def essen(self):
        pass


class Hund(Tier):
    def __init__(self, name: str = "Rex"):
        self.name = name

    def essen(self, was):
        print(f"{self.name} isst {was}")


t1 = Hund()
t1.essen("Wurst")
