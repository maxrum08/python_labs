from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.

    По умолчанию используется UTF-8.
    Для другой кодировки можно указать, например, encoding="cp1251".

    Если файл не найден/кодировка неверна, вызывает FileNotFoundError/UnicodeDecodeError.
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки для указанного файла, если их нет."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """
    Записывает строки в CSV-файл с кодировкой UTF-8.

    Если передан header, он записывается первой строкой.
    Если длина строк различается, вызывает ValueError.
    """
    p = Path(path)
    rows = list(rows)

    # Проверяем одинаковую длину всех строк
    if header is not None:
        length = len(header)
    elif rows:
        length = len(rows[0])
    else:
        length = None

    for row in rows:
        if len(row) != length:
            raise ValueError("Все строки CSV должны иметь одинаковую длину")
        
    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

if __name__ == '__main__':
    txt = read_text("data/lab04/input.txt")
    print(txt)
    write_csv([("word","count"),("test",3)], "data/lab04/check.csv")