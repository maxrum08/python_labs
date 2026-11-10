import random
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
 
def check_sorting(fn, trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(original), f"{fn.__name__} ошиблась на {original}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"


def check_search(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-100, 100)

        try:
            expected = nums.index(target)
        except ValueError:
            expected = -1
        assert linear_search(nums, target) == expected

        nums.sort()
        result = binary_search(nums, target)

        if target not in nums:
            assert result == -1
        else:
            assert nums[result] == target


def check_two_sum(trials=100):
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        target = random.randint(-200, 200)
        brute_result = two_sum_brute(nums, target)
        fast_result = two_sum_fast(nums, target)

        if brute_result is None or fast_result is None:
            assert brute_result == fast_result, "Разный результат"
        else:
            i, j = brute_result
            assert nums[i] + nums[j] == target, "Неверная пара в two_sum_brute"
            i, j = fast_result
            assert nums[i] + nums[j] == target, "Неверная пара в two_sum_fast"

 
if __name__ == "__main__":
    random.seed(42)
    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()
    print("OK")