import time
import random

for i in range(1000000):
    pass


def insertion_sort(l):
    for i in range(1, len(l)):
        k = l[i]
        j = i - 1
        while j >= 0 and l[j] > k:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = k

l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

insertion_sort(l)
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")