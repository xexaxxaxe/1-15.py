def filter_monotonic(arr):
    if not arr:
        return [], 0
    res = [arr[0]]
    last_kept = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= last_kept:
            res.append(arr[i])
            last_kept = arr[i]
    return res, len(res)

# Пример из условия
A = [5.5, 2.5, 4.6, 7.2, 5.8, 9.4]
A_new, N_A = filter_monotonic(A)
print(f"Результат (размер {N_A}):", A_new)