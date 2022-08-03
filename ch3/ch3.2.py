from matplotlib import pyplot as plt

movies = ["Энни Холл", "Бен-Гур", "Касабланка", "Ганди", "Вестсайдская история"]
num_oscars = [5, 11, 3, 8, 10]

# Построить стлобцы с левыми X-координатами [xs] и высотами [num_oscars]
plt.bar(range(len(movies)), num_oscars)
plt.title("Мои любимые фильмы")     # Добавить заголовок
plt.ylabel("Количество наград")     # Разместить метку на оси y

# Пометить ось x названиями фильмов в центре каждого столбца
plt.xticks(range(len(movies)), movies)
plt.show()
