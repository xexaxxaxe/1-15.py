def find_max_index(arr):
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[max_idx]:
            max_idx = i
    return max_idx

# Пример
A, B, C = [1.2, 5.5, 2.3], [10.4, 52.1, 7.8], [4.5, 2.1, 89.9]
print("Индекс макс A:", find_max_index(A))
print("Индекс макс B:", find_max_index(B))
print("Индекс макс C:", find_max_index(C))