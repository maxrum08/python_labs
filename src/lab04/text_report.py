
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv


INPUT = Path("data/lab04/input.txt")
OUTPUT = Path("data/lab04/report.csv")
ENCODING = "utf-8"

def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))

text = read_text(INPUT, encoding=ENCODING)
normal = normalize(text)
words = tokenize(normal)
freq = count_freq(words)
top_5 = top_n(freq, 5)
rows = sorted_word_counts(freq)


write_csv(rows, OUTPUT, header=("word", "count"))

print(f'Всего слов: {len(words)}')
print(f'Уникальных слов: {len(set(words))}')
print('Топ-5:')
for place in top_5:
    print(f"{place[0]}:{place[1]}")

