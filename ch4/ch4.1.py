import enum, random


class Kid(enum.Enum):
    BOY = 0
    GIRL = 1


def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])


both_girls = 0
older_girl = 0
either_gir = 0

random.seed(0)


for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:
        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_gir += 1

print("P(both):", both_girls / 10000)
print("P(older):", older_girl / 10000)
print("P(either):", either_gir / 10000)
print("P(both | older):", both_girls / older_girl)
print("P(both | either):", both_girls / either_gir)
