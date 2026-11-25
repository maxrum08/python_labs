import json
from src.lab08.models import student_to_dict
from src.lib.io_txt_csv import read_text

def students_to_json(students: list[dict], path: str) -> None:
    """Сохраняет список валидных записей студентов в JSON файл."""
    valid_students = [student_to_dict(student) for student in students]
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(valid_students, f, ensure_ascii=False, indent=2)

def students_from_json(path: str) -> list[dict]:
    """Читает JSON-массив студентов.
    Strict политика битых записей."""
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка при чтении JSON: {e}")
        
    valid_students = []
    for id, student in enumerate(data, start=1):
        try:
            valid_students.append(student_to_dict(student))
        except ValueError as e:
            raise ValueError(f"Ошибка в записи {id}: {e}")
    return valid_students

if __name__ == "__main__":
    input_path = "data/lab08/students_input.json"
    bad_path = "data/lab08/students_bad.json"
    output_path = "data/lab08/students_output.json"

    students = students_from_json(input_path)

    students_to_json(students, output_path)

    try:
        students_from_json(bad_path)
    except ValueError as e:
        print(f"Ошибка: {e}")
