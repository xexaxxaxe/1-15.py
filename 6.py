def smooth_step_v6(arr):
    prev = arr[0]
    for k in range(1, len(arr)):
        curr = arr[k]
        arr[k] = (prev + curr) / 2.0
        prev = curr

# Пятикратное сглаживание
A = [10.0, 2.0, 18.0, 4.0, 30.0]
print("Исходный:", A)
for step in range(1, 6):
    smooth_step_v6(A)
    print(f"Шаг {step}:", A)