import time
import random

for i in range(1000000):
    pass


def bogo_sort(l):
    while not all(l[i] <= l[i + 1] for i in range(len(l) - 1)):
        random.shuffle(l)
    return l


l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

bogo_sort(l)
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")
