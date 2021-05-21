import click
from .common_functions import generate_data as gd
from .common_functions import load_testing_measurements as ms


@click.main()
def main():
    pass


@main.group()
@click.command()
@click.option('--start', type=int, default=5)
@click.option('--end', type=int, default=22)
@click.option('--step', type=int, default=5)
@click.option('--count', type=int, default=5)
def generate_data(start: int, end: int, step: int, count: int):
    try:
        os.mkdir('load_testing_data')
    except OSError:
        pass
    gd.generate_data(start, end, step, count)


@main.group()
@click.command()
@click.argument('name_file', type=str)
def measure_time(name_file:str):
    try:
        os.mkdir('load_testing_measurements')
    except OSError:
        pass
    ms.measure_time(name_file)


@main.group()
@click.option('--file')
def create_chart(file: str):
    ms.draws_graph(file)

