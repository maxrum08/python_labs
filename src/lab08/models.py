from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def make_student(fio: str, birthdate: str, group: str, gpa:float) -> dict:
    """Создает словарь с данными студента, проверяя корректность данных."""
     
    if not isinstance(fio, str) or not isinstance(group, str) or not fio.strip() or not group.strip() or not isinstance(birthdate, str):
        raise ValueError("Поля 'fio' и 'group' должны быть непустыми строками.")
    
    try:
        bd = date.fromisoformat(birthdate)
    except ValueError:
        raise ValueError(f"Некорректная дата рождения: '{birthdate}'. Ожидается YYYY-MM-DD.")
    if bd > date.today():
        raise ValueError(f"Дата рождения '{birthdate}' не может быть в будущем.")

    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)):
        raise ValueError(f"Неверный формат GPA: {gpa}. Ожидается float или int.")
    if not (0.0 <= float(gpa) <= 5.0):
        raise ValueError("GPA должен принадлежать диапазону от 0.0 до 5.0")
     

    return {"fio": fio.strip(), "birthdate": birthdate.strip(), "group": group.strip(), "gpa": float(gpa)}


def validate_student(rec: dict) -> None:
    """Проверяет готовый словарь на валидность данных."""
    if not isinstance(rec, dict):
        raise ValueError("Запись должна быть словарем.")
    
    if set(rec.keys()) != set(STUDENT_FIELDS):
        raise ValueError(f"Неверный набор ключей. Получено: {tuple(rec.keys())}, ожидалось: {STUDENT_FIELDS}.")
    
    make_student(rec["fio"], rec["birthdate"], rec["group"], rec["gpa"])

def student_age(rec: dict, today: date | None = None)-> int:
    validate_student(rec)
    b = date.fromisoformat(rec["birthdate"])
    if today is None:
        today = date.today()
    age = today.year - b.year
    if (today.month, today.day) < (b.month, b.day):
        age -= 1
    return age


def student_to_dict(rec):
    """Возвразает копию словаря с данными студента, проверяя корректность данных."""
    validate_student(rec)
    return dict(rec)


def student_from_dict(d):
    """Десериализует словарь, доставая только нужные ключи и проверяет запись через валидацию."""
    if not isinstance(d, dict):
        raise ValueError("Ожидался словарь для десериализации студента.")
    
    fio = d.get("fio")
    birthdate = d.get("birthdate")
    group = d.get("group")
    gpa = d.get("gpa")

    return make_student(fio, birthdate, group, gpa)


def format_student(rec):
    validate_student(rec)
    fio = rec["fio"].split()
    f = fio[0].capitalize()
    io = "".join(f"{part[0].upper()}." for part in fio[1:])
    
    age = student_age(rec)

    return f"{f} {io} ({rec['group']}), {age} лет, GPA {rec['gpa']:.2f}"

if __name__ == "__main__":
    # Пример использования функций
    student = make_student("Руманов Максим Ильич", "2008-06-18", "БИВТ-26-6-5", 4.2)
    print(f"Студент: {student}")
    print(f"Возраст студента: {student_age(student)} лет")
    print(f"Форматированная запись: {format_student(student)}")

    print("Проверка валидации:")
    try:
        invalid_student = make_student("Клод Клодович", "2020-02-30", "БИВТ-26-6-2", 6.7)
    except ValueError as e: 
        print(f"Ошибка: {e}")

