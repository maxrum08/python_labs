def format_record(rec: tuple[str, str, float]) -> str:
    '''Возвращает отформатированную запись студента.'''

    if not isinstance(rec, tuple): raise TypeError('Неверный тип данных')
    if len(rec) != 3: raise ValueError('Неверное число данных')
    if not isinstance(rec[0], str): raise TypeError('Неверный тип ФИО')
    if not isinstance(rec[1], str): raise TypeError('Неверный тип группы')
    if not isinstance(rec[2], (int, float)): raise TypeError('Неверный тип GPA')
    if not rec[0].strip(): raise ValueError('Пустое ФИО')
    if not rec[1].strip(): raise ValueError('Пустая группа')
    if not 0.0 <=rec[2] <= 5.0: raise ValueError("Неверное значение GPA")

    fio, group, gpa = rec
    s_fio = fio.split()
    if len(s_fio) < 2 or len(s_fio)>3: raise ValueError('Неверное ФИО')

    if len(s_fio) == 2:
        f, i = s_fio
        name = f'{f[0].upper()+f[1:].lower()} {i[0].upper()}.'

    elif len(s_fio) == 3:
        f, i, o = s_fio
        name = f'{f[0].upper()+f[1:].lower()} {i[0].upper()}.{o[0].upper()}.'

    return f'{name}, гр. {group.strip()}, GPA {gpa:.2f}'

if __name__ == '__main__':
    for test in (("Иванов Иван Иванович", "BIVT-25", 4.6),
                 ("Петров Пётр", "IKBO-12", 5.0),
                 ("Петров Пётр Петрович", "IKBO-12", 5.0),
                 ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
                 ("Макс", "bimbimbambam", 5.00)):
        print(test, '=> ', end = '')
        print(format_record(test))