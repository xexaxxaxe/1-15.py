def find_min_max_indices(arr):
    min_idx, max_idx = 0, 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
        if arr[i] > arr[max_idx]:
            max_idx = i
    return min_idx, max_idx

# Пример
A = [3.5, 1.2, 9.8, 0.4, 7.1]
n_min, n_max = find_min_max_indices(A)
print(f"A -> Индекс мин: {n_min}, Индекс макс: {n_max}")