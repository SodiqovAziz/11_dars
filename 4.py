from abc import ABC, abstractmethod

class Bola(ABC):
    def __init__(self, ism):
        self.ism = ism
        self.kitob_soni = 0
        self.pul = 0

    @abstractmethod
    def kitob_oqish(self, soni):
        pass

    def malumot_ol(self):
        return f"{self.ism} - Kitoblar soni: {self.kitob_soni}, Pul: {self.pul} so`m"


class Bola1(Bola):
    def kitob_oqish(self, soni):
        self.kitob_soni += soni
        self.pul = self.kitob_soni * 1000


class Bola2(Bola):
    def kitob_oqish(self, soni):
        self.kitob_soni += soni
        self.pul = self.kitob_soni * 1000


bola1 = Bola1("Bola1")
bola2 = Bola2("Bola2")

bola1.kitob_oqish(3)
bola2.kitob_oqish(5)

print(bola1.malumot_ol())
print(bola2.malumot_ol())
