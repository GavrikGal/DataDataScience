from matplotlib import pyplot as plt

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]  # Друзья
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]  # Минуты
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']   # Метки

plt.scatter(friends, minutes)

# назначить метку для каждой точки
for label, friend_count, minute_count in zip(labels, friends, minutes):
    plt.annotate(label,
                 xy=(friend_count, minute_count),  # задать метку
                 xytext=(5, -5),                   # и немного сместить ее
                 textcoords='offset points')
plt.title("Число минут против числа друзей")
plt.xlabel("Число друзей")
plt.ylabel("Число минут, проводимых на сайте ежедневно")
plt.show()

