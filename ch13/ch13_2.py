from io import BytesIO      # Необходимо трактовать байты как файл.
import requests             # Для скачивания файлов, которые
import tarfile              # находятся в формате .tar.bz


BASE_URL = "https://spamassassin.apache.org/old/publiccorpus"
FILES = ["20021010_easy_ham.tar.bz2",
         "20021010_hard_ham.tar.bz2",
         "20021010_spam.tar.bz2"]

# В этих папках данные окажутся после распаковки:
# /spam, /easy_ham, /hard_ham.
# Можете поменять каталог по своему желанию
OUTPUT_DIR = 'spam_data'

for filename in FILES:
    # Используем requests для получения
    # содержимого файлов в каждом URL
    content = requests.get(f"{BASE_URL}/{filename}").content

    # Обернуть байты в памяти, чтобы использовались как "файл"
    fin = BytesIO(content)

    # И извлечь все файлы в указанный выходной каталог.
    with tarfile.open(fileobj=fin, mode='r:bz2') as tf:
        tf.extractall(OUTPUT_DIR)
