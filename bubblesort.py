import time
import random

for i in range(1000000):
    pass


def bubble_sort(l):
    n = len(l)
    k = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if l[j] > l[j + 1]:
                k += 1
                l[j], l[j + 1] = l[j + 1], l[j]


l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

bubble_sort(l)
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")
