def create_index_array(arr):
    # Возвращает массив индексов, отсортированных по значениям arr
    return sorted(range(len(arr)), key=lambda i: arr[i])

# Пример
A = [5.5, 2.5, 4.6, 7.2]
I = create_index_array(A)
print("Исходный массив:", A)
print("Индексный массив:", I)