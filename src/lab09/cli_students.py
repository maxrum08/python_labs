import argparse
import sys

from src.lab08.models import format_student, make_student
from src.lab09.group import add_student, find_students, list_students, remove_student, update_student

PATH = "data/lab09/students.csv"


def main() -> int:
    """Запускает CLI для работы с базой студентов."""
    parser = argparse.ArgumentParser(description="Учёт студентов в CSV-файле")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="добавить студента")
    add_parser.add_argument("--fio", required=True, help="ФИО студента")
    add_parser.add_argument("--birthdate", required=True, help="дата рождения YYYY-MM-DD")
    add_parser.add_argument("--group", required=True, help="учебная группа")
    add_parser.add_argument("--gpa", type=float, required=True, help="средний балл от 0 до 5")

    list_parser = subparsers.add_parser("list", help="показать студентов")
    list_parser.add_argument("--sort", choices=("fio", "gpa"), help="сортировка списка")

    find_parser = subparsers.add_parser("find", help="найти по ФИО")
    find_parser.add_argument("--q", required=True, help="подстрока для поиска")

    remove_parser = subparsers.add_parser("remove", help="удалить по ФИО")
    remove_parser.add_argument("--fio", required=True, help="ФИО студента")

    update_parser = subparsers.add_parser("update", help="обновить студента")
    update_parser.add_argument("--fio", required=True, help="ФИО студента")
    update_parser.add_argument("--birthdate", help="новая дата рождения YYYY-MM-DD")
    update_parser.add_argument("--group", help="новая учебная группа")
    update_parser.add_argument("--gpa", type=float, help="новый средний балл")

    args = parser.parse_args()

    try:
        if args.command == "add":
            student = make_student(args.fio, args.birthdate, args.group, args.gpa)
            add_student(PATH, student)
            print(f"Добавлен: {format_student(student)}")

        elif args.command == "list":
            students = list_students(PATH, args.sort)
            if not students:
                print("Студентов нет.")
            for student in students:
                print(format_student(student))

        elif args.command == "find":
            students = find_students(PATH, args.q)
            if not students:
                print("Ничего не найдено.")
            for student in students:
                print(format_student(student))

        elif args.command == "remove":
            removed_count = remove_student(PATH, args.fio)
            print(f"Удалено записей: {removed_count}")

        elif args.command == "update":
            fields = {}
            if args.birthdate is not None:
                fields["birthdate"] = args.birthdate
            if args.group is not None:
                fields["group"] = args.group
            if args.gpa is not None:
                fields["gpa"] = args.gpa

            if not fields:
                raise ValueError("Укажите хотя бы одно поле для обновления.")
            if update_student(PATH, args.fio, **fields):
                print(f"Обновлено: {args.fio}")
            else:
                print(f"Ошибка: студент не найден: {args.fio}", file=sys.stderr)
                return 1
    except (TypeError, ValueError, KeyError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)



if __name__ == "__main__":
    raise SystemExit(main())
