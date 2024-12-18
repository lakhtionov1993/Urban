import threading
import random
import time


class Bank(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            number_1 = random.randint(50, 500)
            self.balance += number_1
            print(f'Пополнение: {number_1}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            number_2 = random.randint(50,500)
            print(f'Запрос на {number_2}')
            if self.balance >= number_2:
                self.balance -= number_2
                print(f'Снятие: {number_2}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
