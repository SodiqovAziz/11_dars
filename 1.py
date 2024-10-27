from abc import ABC, abstractmethod

class Ota(ABC):
    def init(self, name):
        self.name = name

    @abstractmethod
    def javob(self):
        pass

class Katta(Ota):
    def javob(self):
        return "Ruxsat bor"

class Kichik(Ota):
    def javob(self):
        return "Ruxsat yo'q"

ogil1 = Katta()
ogil2 = Kichik()

print(ogil2.javob())