def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    '''Возвращает (min, max).'''
    if not nums:
        raise ValueError("Список пуст")
    mn = mx = nums[0]
    for num in nums:
        if num < mn:
            mn = num
        if num > mx:
            mx = num
    return (mn, mx)

# if __name__ == '__main__':
#     print('min_max')
#     for test in ([3, -1, 5, 5, 0], [42], [-5, -2, -9], [1.5, 2, 2.0, -3.1],[]):
#         print(test,'=> ', end ='')
#         print(min_max(test))


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    '''Возвращает отсортированный список уникальных элементов.'''
    unique = list(set(nums))
    for i in range(1, len(unique)):
        current = unique[i]
        j = i - 1
        while j>=0 and unique[j] > current:
            unique[j+1] = unique[j]
            j -= 1
        unique[j+1] = current
    return unique

# if __name__ == '__main__':
#     print('unique_sorted')
#     for test in ([3, 1, 2, 1, 3], [], [-1, -1, 0, 2, 2], [1.0, 1, 2.5, 2.5, 0]):
#         print(test,'=> ', end ='')
#         print(unique_sorted(test))

def flatten(mat: list[list | tuple]) -> list:
    '''Расплющивает список списков/кортежей в один список.'''
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("строка не строка строк матрицы")
        for element in row:
            result.append(element)
    return result

# if __name__ == '__main__':
#     print('flatten')
#     for test in ([[1, 2], [3, 4]], [[1, 2], (3, 4, 5)], [[1], [], [2, 3]], [[1, 2], "ab"]):
#         print(test,'=> ', end ='')
#         print(flatten(test))

