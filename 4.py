def invert_array(arr):
    n = len(arr)
    for i in range(n // 2):
        arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
    return arr

# Пример
A = [1.0, 2.0, 3.0, 4.0, 5.0]
invert_array(A)
print("Инвертированный A:", A)