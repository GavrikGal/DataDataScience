from collections import Counter
from matplotlib import pyplot as plt

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Скруппировать оценки подецильно, но
# разместить 100 вместе с отметками 90 и выше

histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],  # сдвинуть столбец влево на 5
        list(histogram.values()),           # высота столбца
        9.8)                                 # ширина каждого столбца 10

plt.axis([-5, 105, 0, 5])                   # Ось x от -5 до 105, ось y от 0 до 5
plt.xticks([10 * i for i in range(11)])     # Метки по оси x: 0, 10, .... , 100
plt.xlabel("Дециль")
plt.ylabel("Число студентов")
plt.title("Распределение оценок за экзамен №1")
plt.show()
