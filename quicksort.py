import time
import random

for i in range(1000000):
    pass


def quicksort(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l) // 2]
    L = [x for x in l if x < pivot]
    mid = [x for x in l if x == pivot]
    R = [x for x in l if x > pivot]
    return quicksort(L) + mid + quicksort(R)


l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

print(quicksort(l))
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")
