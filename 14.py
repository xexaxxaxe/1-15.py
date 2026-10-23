def split_by_indices(arr):
    # Порядковые номера 1, 3, 5... (нечетные) -> индексы 0, 2, 4... в Python
    # Порядковые номера 2, 4, 6... (четные) -> индексы 1, 3, 5... в Python
    B = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    C = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    return B, len(B), C, len(C)

# Пример
A = [10.0, 20.0, 30.0, 40.0, 50.0]
B, Nb, C, Nc = split_by_indices(A)
print(f"B (нечетные позиции, размер {Nb}):", B)
print(f"C (четные позиции, размер {Nc}):", C)