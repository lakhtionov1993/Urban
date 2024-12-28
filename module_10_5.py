from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line_file = file.readline().strip()
            all_data.append(line_file)
            if not line_file:
                break


if __name__ == '__main__':
    file_number = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    line_start = datetime.now()
    for i in file_number:
        read_info(i)
    line_end = datetime.now()

    mult_start = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, file_number)
    mult_end = datetime.now()

    line_function = line_end - line_start
    multiprocessing = mult_end - mult_start

    print(f'{line_function} (линейный)')
    print(f'{multiprocessing} (многопроцессный)')
