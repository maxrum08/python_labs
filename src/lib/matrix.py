def check(mat: list[list[float | int]]) -> bool:
    '''Проверка матрицы на "рваность".'''
    if not mat:
        return True
    col = len(mat[0])
    for row in mat:
        if len(row) != col:
            return False
    return True

def transpose(mat: list[list[float | int]]) -> list[list]:
    '''Транспонирует матрицу.'''
    if mat == []:
        return []
    if not check(mat):
        raise ValueError('рваная матрица')
    rows = len(mat)
    cols = len(mat[0])
    tmat=[]
    for i in range(cols):
        row=[]
        for j in range(rows):
            row.append(mat[j][i])
        tmat.append(row)
    return tmat

# if __name__ == '__main__':
#     print('transpose')
#     for test in ([[1, 2, 3]], [[1], [2], [3]], [[1, 2], [3, 4]], [], [[1, 2], [3]]):
#         print(test,'=> ', end ='')
#         print(transpose(test))

def row_sums(mat: list[list[float | int]]) -> list[float]:
    '''Возвращает список сумм каждой строки матрицы.'''
    if not check(mat):
        raise ValueError('рваная матрица')
    sums=[]
    for i in range(len(mat)):
        sums.append(sum(mat[i]))
    return sums

# if __name__ == '__main__':
#     print('row_sums')
#     for test in ([[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]):
#         print(test,'=> ', end ='')
#         print(row_sums(test))

def col_sums(mat: list[list[float | int]]) -> list[float]:
    '''Возвращает список сумм каждого столбца матрицы.'''
    return row_sums(transpose(mat))

# if __name__ == '__main__':
#     print('col_sums')
#     for test in ([[1, 2, 3], [4, 5, 6]], [[-1, 1], [10, -10]], [[0, 0], [0, 0]], [[1, 2], [3]]):
#         print(test,'=> ', end ='')
#         print(col_sums(test))