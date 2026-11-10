def bubble_sort(nums):
    '''Сортировка пузырьком. Возвращает новый список, не меняя исходный.
    Добавлен флаг обменов: если на проходе ничего не менялось, список уже отсортирован.'''
    result = list(nums)
    n = len(result)
    for i in range(n):
        swap = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swap = True
        if not swap:
            break
    return result


def insertion_sort(nums):
    '''Сортировка вставками. Возвращает новый список, не меняя исходный.'''
    result = list(nums)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def selection_sort(nums):
    '''Сортировка выбором. Возвращает новый список, не меняя исходный.'''
    result = list(nums)
    n = len(result)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if result[j] < result[min_index]:
                min_index = j
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]
    return result