def bell_sort(arr):
    sorted_arr = sorted(arr)
    res = [0.0] * len(arr)
    left, right = 0, len(arr) - 1
    
    for i in range(len(sorted_arr)):
        if i % 2 == 0:
            res[left] = sorted_arr[i]
            left += 1
        else:
            res[right] = sorted_arr[i]
            right -= 1
            
    # Записываем результат обратно в исходный массив
    for i in range(len(arr)):
        arr[i] = res[i]
    return arr

# Пример
A = [5.0, 1.0, 3.0, 2.0, 4.0]
bell_sort(A)
print("«Колокол»:", A)