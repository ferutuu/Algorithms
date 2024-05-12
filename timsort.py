import time
import random

for i in range(1000000):
    pass


def insertion_sort(l, L=0, R=None):
    if R is None:
        R = len(l) - 1

    for i in range(L + 1, R + 1):
        k = l[i]
        j = i - 1
        while j >= L and l[j] > k:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = k

    return l


def merge_sort(l, L, mid, R):
    len1, len2 = mid - L + 1, R - mid
    left, right = l[L:mid + 1], l[mid + 1:R + 1]

    i, j, k = 0, 0, L
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        else:
            l[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        l[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        l[k] = right[j]
        j += 1
        k += 1


def timsort(l):
    m = 32
    n = len(l)

    for start in range(0, n, m):
        end = min(start + m - 1, n - 1)
        insertion_sort(l, start, end)

    size = m
    while size < n:
        for L in range(0, n, 2 * size):
            mid = min(n - 1, L + size - 1)
            R = min((L + 2 * size - 1), (n - 1))
            if mid < R:
                merge_sort(l, L, mid, R)
        size = 2 * size


l = []
start_time = time.perf_counter()
for i in range(0, 10000000):
    x = random.randint(1, 100000)
    l.append(x)

timsort(l)
print(l)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"Code execution time: {execution_time:.10f} seconds")
