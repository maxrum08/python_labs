import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from pathlib import Path
from src.lab05.json_csv import check_ext


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
	"""
    Конвертирует CSV в XLSX.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
	check_ext(csv_path, ".csv")
	check_ext(xlsx_path, ".xlsx")
	wb = Workbook()
	ws = wb.active
	column_widths = {}

	with open(csv_path, "r", encoding="utf-8", newline="") as file:
		rows = list(csv.reader(file))
		if not rows: raise ValueError("CSV-файл пустой")
		for row in rows:
			ws.append(row)
			for i, value in enumerate(row, start=1):
				column_widths[i] = max(column_widths.get(i, 0), len(value))

	for i, width in column_widths.items():
		ws.column_dimensions[get_column_letter(i)].width = max(8, width)
		
	output = Path(xlsx_path)
	output.parent.mkdir(parents=True, exist_ok=True)
	wb.save(output)

if __name__ == "__main__":
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")