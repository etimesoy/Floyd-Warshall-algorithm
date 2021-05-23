# Floyd–Warshall algorithm

## Сам алгоритм:

Алгоритм Флойда — Уоршелла — алгоритм для нахождения кратчайших расстояний между всеми вершинами взвешенного графа без
циклов с отрицательными весами с использованием метода динамического программирования.

## Как работает:

Имеется кратчайший путь p1k=(v1,v2,… ,vk) от вершины v1 до вершины vk, а также его подпуть p'(vi,vi+1,… ,vj), при этом
действует 1 <= i <= j <= k.

<p>Если p — кратчайший путь от v1 до vk, то p' также является кратчайшим 
путем от вершины vi до vj</p>

<p>Это можно легко доказать, так как стоимость пути p складывается из стоимости
пути p' и стоимости остальных его частей. Так вот представив что есть более 
короткий путь p', мы уменьшим эту сумму, что приведет к противоречию с утверждением, 
что эта сумма и так уже была минимальной.</p>

<p> Второе свойство является основой алгоритма. Мы рассматриваем граф G 
с пронумерованными от 1 до n вершинами {v1,v2,… ,vn} и путь pij от vi до vj, 
проходящий через определенное множество разрешенных вершин, ограниченное индексом k.</p>

<p>То есть если k=0, то мы рассматриваем прямые соединения вершин друг с другом, 
так как множество разрешенных промежуточных вершин равно нулю.
Если k=1 — мы рассматриваем пути, проходящие через вершину v1, 
при k=2 — через вершины {v1, v2}, при k=3 — {v1, v3, v3} и так далее.</p>

## Где используется:

<p>Как и любой базовый алгоритм, алгоритм Флойда — Уоршелла 
используется очень широко и много где, начиная от поиска транзитивного замыкания графа, 
заканчивая генетикой и управлением проектами. Но первое что приходит в голову конечно же 
транспортные и всякие другие сети.</p>

<p>Скажем если вы возьмете карту города — её транспортная система это граф, 
соответственно присвоив каждому ребру некую стоимость, 
рассчитанную скажем из пропускной способности и других важный параметров — вы сможете 
подвезти попутчика по самому короткому/быстрому/дешевому пути.</p>

## Как запустить?

Вам потребуется Python 3.8 или выше

1. pip install floyd-warshall-alg
2. Вызовите floyd_alg --help, чтобы убедиться, что он успешно установлен

## Команды

* process-one запускает алгоритм


* generate_data --start 1 --end 22 --step 10 --count 5 (выполняет генерацию данных и их сохранение в директорию load_testing_data/)


* measure-time замеряет время выполнения программы на ранее сгенерированных тестовых данных, результат сохраняется в
  load_testing_measurements


* create-chart --file 1620506940 принимает на вход путь до csv файла, который был создан на предыдущем шаге, и рисует график, который
  сохраняется в директории load_testing_plots

### Пример графика:

![Alt text](load_testing_plots/1621626290.png?raw=true "Title")
[![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/RBBIM4YO2_8)
