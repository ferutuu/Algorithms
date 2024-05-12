import time
import random

for i in range(1000000):
    pass


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        L = l[: mid]
        R = l[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                l[k] = L[i]
                i += 1
            else:
                l[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            l[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            l[k] = R[j]
            j += 1
            k += 1


l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

merge_sort(l)
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")
