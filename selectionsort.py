import time
import random

for i in range(1000000):
    pass


def selection_sort(l):
    n = len(l)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if l[j] < l[min]:
                min = j
        l[i], l[min] = l[min], l[i]


l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

selection_sort(l)
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")