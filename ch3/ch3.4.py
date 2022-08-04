from matplotlib import pyplot as plt

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]   # Дисперсия
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]   # Квадрат смещения
# Суммарная ошибка
total_error = [x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

# Метод plt.plot можно вызывать много раз,
# чтобы показать несколько графиков на одной и той же диаграмме:
# Зеленая сплошная линия
plt.plot(xs, variance, 'g-', label='дисперсия')
# Красная штрихпунктирная
plt.plot(xs, bias_squared, 'r-.', label='смещение^2')
# Синяя пунктирная
plt.plot(xs, total_error, 'b:', label='суммарная ошибка')
# Если для каждой линии задано label,
# то легенда будет показана автоматически,
# loc=9 означает "наверху посередине"
plt.legend(loc=9)
plt.xlabel("Сложность модели")
plt.title("Компромисс между смещением и дисперсией")
plt.show()

