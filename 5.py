from abc import ABC, abstractmethod

class Bola(ABC):
    def __init__(self, ism):
        self.ism = ism
        self.kitoblar = []
        self.pul = 0

    @abstractmethod
    def kitob_oqish(self, kitob_nomi):
        pass

    def kitobni_qidir(self, kitob_nomi):
        """Berilgan kitobni qaysi bola o'qiganini tekshiradi."""
        if kitob_nomi in self.kitoblar:
            return f"{kitob_nomi} kitobini {self.ism} o'qigan."
        return None


class Bola1(Bola):
    def kitob_oqish(self, kitob_nomi):
        self.kitoblar.append(kitob_nomi)
        self.pul = len(self.kitoblar) * 1000


class Bola2(Bola):
    def kitob_oqish(self, kitob_nomi):
        self.kitoblar.append(kitob_nomi)
        self.pul = len(self.kitoblar) * 1000


def kitob_qidirish(kitob_nomi, bolalar):
    for bola in bolalar:
        natija = bola.kitobni_qidir(kitob_nomi)
        if natija:
            return natija
    return f"{kitob_nomi} kitobini hech kim o'qimagan."


bola1 = Bola1("Bola1")
bola2 = Bola2("Bola2")

bola1.kitob_oqish("Matematika")
bola2.kitob_oqish("Fizika")
bola1.kitob_oqish("Tarix")

print(kitob_qidirish("Matematika", [bola1, bola2]))
print(kitob_qidirish("Fizika", [bola1, bola2]))
print(kitob_qidirish("Geografiya", [bola1, bola2]))