# Наиболее распространеные слова
import sys
from collections import Counter


# Передать число слов в качестве первого аргумента
try:
    num_words = int(sys.argv[1])
except:
    print("Применение: most_common_words.py num_words")
    sys.exit(1)     # Ненулевой код выхода сигнализирует об ошибке

counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()      # Разбить строку по пробелам
                  if word)                              # Пропустить 'пустые' слова

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")
