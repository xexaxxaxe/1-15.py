def duplicate_element(arr, x):
    res = []
    for val in arr:
        res.append(val)
        if val == x:
            res.append(x)
    return res, len(res)

# Пример
A, Xa = [1, 5, 3, 5, 2], 5
A_new, N_A = duplicate_element(A, Xa)
print(f"Результат (размер {N_A}):", A_new)