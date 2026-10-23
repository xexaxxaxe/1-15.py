def remove_element(arr, x):
    res = [val for val in arr if val != x]
    return res, len(res)

# Пример
A, Xa = [1, 5, 3, 5, 7, 5, 2], 5
A_new, N_A = remove_element(A, Xa)
print(f"Новый массив (размер {N_A}):", A_new)