from typing import List
from collections import Counter
import glob
import random
from scratch.machine_learning import split_data
from ch13_1 import Message, NaiveBayesClassifier


# Замените этот путь на любой каталог, в который вы поместили файлы
path = 'spam_data/*/*'

data: List[Message] = []
# glob.glob возвращает каждое имя файла,
# которое соответствует поисковому шаблону пути
for filename in glob.glob(path):
    is_spam = "ham" not in filename

    # В письмах имеются несколько мусорных символов;
    # параметр errors = 'ignore' пропускает их вместо вызова исключения
    with open(filename, errors='ignore') as email_file:
        for line in email_file:
            if line.startswith("Subject:"):
                subject = line.lstrip("Subject: ")
                data.append(Message(subject, is_spam))
                break   # С этим файлом работа закончена

random.seed(0)
train_messages, test_messages = split_data(data, 0.75)

model = NaiveBayesClassifier()
model.train(train_messages)

predictions = [(message, model.predict(message.text))
               for message in test_messages]

confusion_matrix = Counter((message.is_spam, spam_probability > 0.5)
                           for message, spam_probability in predictions)

print(confusion_matrix)


def p_spam_given_token(token: str, model: NaiveBayesClassifier) -> float:
    # Не следует вызывать приватные методы, но надо
    prob_if_spam, prob_if_ham = model._probabilities(token)

    return prob_if_spam / (prob_if_spam + prob_if_ham)


words = sorted(model.tokens, key=lambda t: p_spam_given_token(t, model))


print("Наиболее спамные слова: ", words[-10:])
print("Наименее спамные слова: ", words[:10])
