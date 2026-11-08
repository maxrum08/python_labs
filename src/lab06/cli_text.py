import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n


def cat(path: str, n: bool) -> None:
    with Path(path).open('r', encoding='utf-8') as f:
        if n:
            for i, line in enumerate(f.readlines()):
                print(i, line.rstrip())
        else:
            for line in f.readlines():
                print(line.rstrip())

def stats(path: str, top: int):
    with Path(path).open('r', encoding='utf-8') as f:
        text = f.read()
        tokens = tokenize(normalize(text))
    print(f'Всего слов: {len(tokens)}')
    print(f'Уникальных слов: {len(set(tokens))}')
    print(f'Топ-{top}:')
    for place in top_n(count_freq(tokens), top):
        print(f"{place[0]}:{place[1]}")

            

 

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла", description="Выводит файл в консоль; с -n нумерует строки.")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов", description="Выводит частоты слов в файле.")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cat(args.input, args.n)
    elif args.command == "stats":
        stats(args.input, args.top)


if __name__ == "__main__":
    main()