import sys, re


# sys.argv - список командной строки
# sys.argv[0] - имя самой программы
# sys.argv[1] - регулярное выражение, указываемое в командной строке
regex = sys.argv[1]

# Для каждой строки, переданной сценарию
for line in sys.stdin:
    # если она соответствует регулярному выражению regex,
    # то записать ее в stdout
    if re.search(regex, line):
        sys.stdout.write(line)
