import random
import os

"""
Функция должна работать по принципу функции range, принимая параметры start, end, step. 
Эти параметры обозначают размеры нагрузочных тестов. 
В дополнении к этому функция должна принимать параметр count - 
сколько разных нагрузочных тестов одного размера нужно сгенерировать. 

Пример использования - generate(start=1, end=22, step=10, count=5) -
генерирует 5 нагрузочных тестов с размером данных 1, 5 нагрузочных тестов с размером данных 11, 5 нагрузочных тестов 
с размером данных 21.

R.D Вы можете сделать кол-вом (которое фигурирует в задании) кол-во вершин в графе, а рёбра рандомно выставлять
"""


# название файлов РАЗМЕР_НОМЕР.РАСШИРЕНИЕ


def generate_data(start: int, end: int, step: int, count: int):
    for i in range(start, end, step):
        for j in range(1, count + 1):
            with open(f'load_testing_data\\{i}_{j}.txt', 'w') as file:
                len_vertex = random.randint(start, i)
                len_ribs = random.randint(start, end)
                file.write(f'{len_vertex}\n')
                file.write(f'{len_ribs}\n')
                for q in range(len_ribs):
                    file.write(f'{random.randint(1, len_vertex)} {random.randint(1, len_vertex)} '
                               f'{random.randint(start, end)}\n')


def main():
    try:
        os.mkdir('load_testing_data')
    except OSError:
        pass

    start = int(input('input start: '))
    end = int(input('input end: '))
    step = int(input('input step: '))
    count = int(input('input count: '))

    generate_data(start, end, step, count)


if __name__ == '__main__':
    main()
