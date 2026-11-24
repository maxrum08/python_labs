import csv
from pathlib import Path

from src.lab08.models import STUDENT_FIELDS, student_from_dict, validate_student

HEADER = STUDENT_FIELDS


def ensure_storage(path):
    """Создает CSV-файл с заголовком, если его еще нет."""
    storage_path = Path(path)
    if not storage_path.exists():
        storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(storage_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER)


def load_students(path) -> list[dict]:
    """Читает и проверяет записи в CSV."""
    ensure_storage(path)
    students = []

    with open(path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != list(HEADER):
            raise ValueError("Некорректная структура заголовков CSV-файла.")

        for line_number, row in enumerate(reader, start=2):
            try:
                if None in row or None in row.values():
                    raise ValueError("число значений не совпадает с заголовком")
                row["gpa"] = float(row["gpa"])
                student = student_from_dict(row)
                validate_student(student)
            except (KeyError, ValueError, TypeError) as e:
                raise ValueError(f"Ошибка валидации данных в строке {line_number}: {e}")
            students.append(student)

    return students


def save_students(path, students):
    """Перезаписывает CSV-файл списком студентов."""
    storage_path = Path(path)
    storage_path.parent.mkdir(parents=True, exist_ok=True)
    for student in students:
        validate_student(student)

    with open(storage_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(students)


def add_student(path, student: dict):
    """Проверяет и добавляет студента; повторение ФИО запрещено."""
    validate_student(student)
    students = load_students(path)

    for existing_student in students:
        if existing_student["fio"].lower() == student["fio"].lower():
            raise ValueError(f"Студент с ФИО '{student['fio']}' уже есть в базе данных.")

    students.append(student)
    save_students(path, students)


def list_students(path, sort_by=None) -> list[dict]:
    students = load_students(path)
    if sort_by is None:
        return students
    if sort_by not in ("fio", "gpa"):
        raise ValueError("Сортировка должна быть по 'fio' или 'gpa'.")
    return sorted(students, key=lambda student: student[sort_by])


def find_students(path, substr: str) -> list[dict]:
    """Ищет студентов по подстроке в ФИО без учета регистра."""
    students = load_students(path)
    found_students = []
    search_text = substr.lower()
    for student in students:
        if search_text in student["fio"].lower():
            found_students.append(student)
    return found_students


def remove_student(path, fio: str) -> int:
    """Удаляет все записи с указанным ФИО и возвращает их количество."""
    students = load_students(path)
    remaining_students = []
    for student in students:
        if student["fio"].lower() != fio.lower():
            remaining_students.append(student)

    removed_count = len(students) - len(remaining_students)
    if removed_count:
        save_students(path, remaining_students)

    return removed_count


def update_student(path, fio: str, **fields) -> bool:
    """Обновляет первую запись с указанным ФИО."""
    for field in fields:
        if field not in HEADER:
            raise KeyError(f"Неизвестное поле для обновления: {field}")

    students = load_students(path)
    for student_index, student in enumerate(students):
        if student["fio"].lower() == fio.lower():
            updated_student = dict(student)
            updated_student.update(fields)
            validate_student(updated_student)
            students[student_index] = updated_student
            save_students(path, students)
            return True

    return False
