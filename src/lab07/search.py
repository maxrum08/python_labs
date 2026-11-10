
def linear_search(nums, x):
    '''Линейный поиск'''
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums, x):
    '''Бинарный поиск. Только для отсортированного списка'''
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sorted_nums[mid] == x:
            return mid
        elif sorted_nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def two_sum_brute(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target: 
                return (i,j)
    return None

def two_sum_fast(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        pair = target - num
        if pair in seen:
            return [seen[pair], i]
        seen[num] = i    
    return None