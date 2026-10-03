
from src.lib.text import normalize, tokenize, count_freq, top_n

text = input()
TABLE = 1

normal = normalize(text)
words = tokenize(normal)
freq = count_freq(words)
top_5 = top_n(freq, 5)

print(f'Всего слов: {len(words)}')
print(f'Уникальных слов: {len(set(words))}')
print('Топ-5:')


if not TABLE:
    for place in top_5:
        print(f"{place[0]}:{place[1]}")
else:
    max_len = max([len(w[0]) for w in top_5] + [len("слово")])
    first_row = f"{'слово':<{max_len}} | частота"
    print(first_row)
    print("-" * (len(first_row)))

    for word in top_5:
        print(f"{word[0]:<{max_len}} | {word[1]}")  

