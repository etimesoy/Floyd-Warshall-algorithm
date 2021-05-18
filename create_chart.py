import matplotlib.pyplot as plt
import csv
import os

size_x = []
min_y1 = []
max_y2 = []
avr_y3 = []
med_y4 = []


def save_to_dir(name: str):
    pwd = os.getcwd()
    path = 'load_testing_plots/'
    if not os.path.exists(path):
        os.mkdir(path)
    os.chdir(path)
    plt.savefig(name.rsplit('.')[0] + '.jpg', format='jpg')
    os.chdir(pwd)


def create_chart(csv_file_path):
    with open(csv_file_path, 'r') as f:
        plots = csv.reader(f, delimiter=',')
        print(plots)
        for column in plots:
            if column:
                if column[0] == 'size':
                    continue
                size_x.append(float(str(column[0]).rsplit('_')[0]))
                min_y1.append(float(column[1]))
                max_y2.append(float(column[2]))
                avr_y3.append(float(column[3]))
                med_y4.append(float(column[4]))


def main():
    path = input()
    create_chart(path)
    plt.plot(size_x, min_y1, label='min')
    plt.plot(size_x, max_y2, label='max')
    plt.plot(size_x, avr_y3, label='avr')
    plt.plot(size_x, med_y4, label='med')
    plt.xlabel('Size')
    plt.ylabel('Time')

    plt.title('')
    plt.legend()

    save_to_dir(path)
    plt.show()


if __name__ == '__main__':
    main()
