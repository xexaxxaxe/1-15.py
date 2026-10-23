def smooth_variant5(arr):
    current_sum = 0
    for k in range(len(arr)):
        current_sum += arr[k]
        arr[k] = current_sum / (k + 1)
    return arr

# Пример
A = [10.0, 20.0, 30.0, 40.0]
smooth_variant5(A)
print("Сглаженный A:", A)