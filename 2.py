from abc import ABC, abstractmethod
class Ota(ABC):
    @abstractmethod
    def __init__(self, ism, yosh):
        self.ism = ism
        self._yosh = yosh

        if self._yosh<18:
            self.pul = 120000000000
            print(f'{self.ism} yoshi - {self._yosh} {self.pul} dan puldan foydalnish mumkin')
        else:
            print(f'{self.ism} yoshi - {self._yosh} Afsus puldan foydalanish mumkin emas')

class bola_1(Ota):
    def __init__(self,ism, yosh):
        super().__init__(ism, yosh)
        self.yosh = yosh

    def haydash(self):
        pass

class bola_2(Ota):
    def __init__(self,ism, yosh):
        super().__init__(ism, yosh)
        self.yosh = yosh

    def haydash(self):
        pass

bola1 = bola_1('Bola1',15)
bola1.haydash()
bola2 = bola_2('Bola2',19)
bola1.haydash()
