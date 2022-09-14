from typing import Dict, List
import csv
from collections import defaultdict
from ch12_1 import LabeledPoint
from scratch.linear_algebra import Vector
from matplotlib import pyplot as plt


def parse_iris_row(row: List[str]) -> LabeledPoint:
    """Длина чашелистика, ширина чашелистика, длина лепестка,
    ширина лепестка, класс"""
    measurements = [float(value) for value in row[:-1]]
    # Классом является, например, "Iris-virginica";
    # нам нужно просто "virginica" (виргинский)
    label = row[-1].split("-")[-1]

    return LabeledPoint(measurements, label)


with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader if len(row) > 0]

# Мы также сгруппируем точки только по виду/метке,
# чтобы их можно было вывести на график
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for iris in iris_data:
    points_by_species[iris.label].append(iris.point)

metrics = ['длн. чашелистика', 'шир. чашелистика', 'длн. лепестка', 'шир. лепестка']
pairs = [(i, j) for i in range(4) for j in range(4) if i < j]
marks = ['+', '.', 'x']     # у нас 3 класса, поэтому 3 метки

fig, ax = plt.subplots(2, 3)

for row in range(2):
    for col in range(3):
        i, j = pairs[3 * row + col]
        ax[row][col].set_title(f"{metrics[i]} против {metrics[j]}", fontsize=5)
        ax[row][col].set_xticks([])
        ax[row][col].set_yticks([])
        for mark, (species, points) in zip(marks, points_by_species.items()):
            xs = [point[i] for point in points]
            ys = [point[j] for point in points]
            ax[row][col].scatter(xs, ys, marker=mark, label=species)

ax[-1][-1].legend(loc='lower right', prop={'size': 6})
# plt.show()
