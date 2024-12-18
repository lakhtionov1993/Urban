import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        day = 0
        print(f'{self.name} , на нас напали!')
        while enemy:
            time.sleep(1.0)
            day += 1
            enemy -= self.power
            print(f'{self.name} сражается {day} дней, осталось {enemy} воинов')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')
