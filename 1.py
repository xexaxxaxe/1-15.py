def find_min(arr):
    min_val = arr[0]
    for x in arr[1:]:
        if x < min_val:
            min_val = x
    return min_val

# Пример применения к A, B, C
A, B, C = [12, 5, 23, -3, 8], [104, 52, 78, 12], [45, 2, 89]
print("Мин A:", find_min(A))
print("Мин B:", find_min(B))
print("Мин C:", find_min(C))