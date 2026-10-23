def smooth_step_v7(arr):
    if len(arr) < 2:
        return
    orig = arr.copy()
    # Первый элемент
    arr[0] = (orig[0] + orig[1]) / 2.0
    # Внутренние элементы
    for i in range(1, len(orig) - 1):
        arr[i] = (orig[i - 1] + orig[i] + orig[i + 1]) / 3.0
    # Последний элемент
    arr[-1] = (orig[-2] + orig[-1]) / 2.0

# Пятикратное сглаживание
A = [10.0, 2.0, 18.0, 4.0, 30.0]
print("Исходный:", A)
for step in range(1, 6):
    smooth_step_v7(A)
    print(f"Шаг {step}:", A)