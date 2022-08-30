from collections import Counter


def get_domain(email_address: str) -> str:
    """Разбить по '@' и вернуть остаток строки"""
    return email_address.lower().split("@")[-1]


# Пара проверок:
assert get_domain('gavrik@gmail.com') == 'gmail.com'
assert get_domain('gavrik@m.datasciencester.com') == 'm.datasciencester.com'


with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f
                            if "@" in line)

print(domain_counts)
