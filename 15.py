def split_by_values(arr):
    B = [x for x in arr if x % 2 == 0]
    C = [x for x in arr if x % 2 != 0]
    return B, len(B), C, len(C)

# Пример
A = [1, 2, 3, 4, 5, 6, 7]
B, Nb, C, Nc = split_by_values(A)
print(f"B (четные числа, размер {Nb}):", B)
print(f"C (нечетные числа, размер {Nc}):", C)