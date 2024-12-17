import threading
import time
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            time.sleep(0.1)
            file.write(f'Какое-то слово № {i+1}' + '\n')
    print(f'Завершилась запись в файл {file_name}')


start_1 = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
stop_1 = datetime.now()
result_1 = stop_1 - start_1

print(f'Время работы функции: {result_1}')


start_2 = datetime.now()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

stop_2 = datetime.now()
result_2 = stop_2 - start_2

print(f'Время работы потоков: {result_2}')
