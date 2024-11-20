import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self,  speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz < 0 and self._cords[2] + self.speed * dz < 0:
            print(f"It's too deep, i can't dive :(")
        else:
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy
            self._cords[2] += self.speed * dz

    def get_cords(self):
        print(f'Х: {int(self._cords[0])} Y: {int(self._cords[1])} Z: {int(self._cords[2])}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")

    def speak(self):
        if self.sound is not None:
            print(self.sound)


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= self.speed * abs(dz) / 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    sound = "Click-click-click"

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        super().lay_eggs()

    def dive_in(self, dz):
        super().dive_in(dz)

    def speak(self):
        super().speak()

    def attack(self):
        super().attack()


if __name__ == '__main__':
    db = Duckbill(10)

    print(db.live)
    print(db.beak)

    db.speak()
    db.attack()

    db.move(1, 2, 3)
    db.get_cords()
    db.dive_in(6)
    db.get_cords()

    db.lay_eggs()
