import pandas as pd
import matplotlib.pyplot as plt


def create_chart(csv_file_path: str):
    data = pd.read_csv(f"{csv_file_path}")
    data.set_index("size", inplace=True)
    data.head()
    data.plot()
    plt.savefig(f'load_testing_plots/{csv_file_path.split("/")[-1].split(".")[0]}.jpg')
    plt.show()


def main():
    path = input("Введите путь до csv файла: ")
    create_chart(path)


if __name__ == '__main__':
    main()
