import random
import timeit
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab04.io_txt_csv import write_csv
 
def bench():
    table = []

    #sorts
    for n in (1000, 10000, 100000):
        data = [random.randint(-100000, 100000) for _ in range(n)]
        time = timeit.timeit(lambda: sorted(data), number=1)
        table.append(("sort", n, "sorted", f"{time:.6f}"))

        if n == 100000:
            table.append(("sort", n, "bubble_sort", "> 60"))
            table.append(("sort", n, "insertion_sort", "> 60"))
            table.append(("sort", n, "selection_sort", "> 60"))
        else:
            time = timeit.timeit(lambda: bubble_sort(data), number=1)
            table.append(("sort", n, "bubble_sort", f"{time:.6f}"))
            
            time = timeit.timeit(lambda: insertion_sort(data), number=1)
            table.append(("sort", n, "insertion_sort", f"{time:.6f}"))
            
            time = timeit.timeit(lambda: selection_sort(data), number=1)
            table.append(("sort", n, "selection_sort", f"{time:.6f}"))
    #searches

    n = 100000
    tasks = 10000
    data = [random.randint(-100000, 100000) for _ in range(n)]
    targets = [random.randint(-100000, 100000) for _ in range(tasks)]
            
    t_linear = timeit.timeit(lambda: [linear_search(data, c) for c in targets], number=1)
    table.append(("search", n, "linear_search", f"{t_linear:.6f}"))
    
    sort_time = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)
            
    time = timeit.timeit(lambda: [binary_search(sorted_data, q) for q in targets], number=1)
    
    table.append(("search", n, "binary_search", f"{time + sort_time:.6f}"))

    #two sum
    for n in (1000, 10000):
        data = [random.randint(-100000, 100000) for _ in range(n)]
        target = random.randint(-100000, 100000)

        time = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
        table.append(("two_sum", n, "two_sum_brute", f"{time:.6f}"))
        
        time = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
        table.append(("two_sum", n, "two_sum_fast", f"{time:.6f}"))
    return table

if __name__ == '__main__':
    table = bench()
    write_csv( table, "data/lab07/bench.csv", header=["task", "n", "algo", "time"])

    print(f'{'task':<10} | {'n':<10} | {'algo':<20} | {'time':<20}')
    print('-' * 70)
    for task, n, algo, time in table:
        print(f'{task:<10} | {n:<10} | {algo:<20} | {time:<20}')
