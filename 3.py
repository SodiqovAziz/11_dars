from abc import ABC, abstractmethod


class Otasi(ABC):
    def __init__(self, ism):
        self.ism = ism
        self.kitoblar = []
        self.pul = 0

    @abstractmethod
    def kitob_qosh(self, varoq_soni):
        pass

    @abstractmethod
    def kitoblar_malumoti(self):
        pass


class Ota(Otasi):
    def kitob_qosh(self, varoq_soni):
        bosma_taboqlar = varoq_soni // 15
        self.kitoblar.append({'varoq_soni': varoq_soni, 'bosma_taboqlar': bosma_taboqlar})

        if bosma_taboqlar > 15:
            self.pul += 13000

    def kitoblar_malumoti(self):
        for i, kitob in enumerate(self.kitoblar, start=1):
            print(f"{i}-kitob: {kitob['varoq_soni']} varoq, {kitob['bosma_taboqlar']} bosma taboq")
        print(f"Jami pul: {self.pul} so'm")

ota = Ota("Alisher")
ota.kitob_qosh(240)
ota.kitob_qosh(300)
ota.kitob_qosh(100)
ota.kitoblar_malumoti()