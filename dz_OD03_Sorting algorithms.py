def merge_sort(arr):
    # Базовый случай: если длина массива 1 или меньше, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Находим середину массива
    mid = len(arr) // 2

    # Рекурсивно сортируем левую и правую половины
    left = merge_sort(arr[:mid])  # Сортировка левой половины
    right = merge_sort(arr[mid:])  # Сортировка правой половины

    # Объединяем отсортированные половины
    return merge(left, right)


def merge(left, right):
    result = []  # Результирующий отсортированный массив
    i, j = 0, 0  # Указатели для левого и правого массивов

    # Сравниваем элементы из левого и правого массивов
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы из левого массива, если они есть
    result.extend(left[i:])

    # Добавляем оставшиеся элементы из правого массива, если они есть
    result.extend(right[j:])

    return result


# Тестирование алгоритма
a = [-3, 5, 0, -8, 1, 10]
print("Исходный массив:", a)

# Вызов функции сортировки
sorted_arr = merge_sort(a)

print("Отсортированный массив:", sorted_arr)

# Пошаговое объяснение работы алгоритма на примере:
print("\nПошаговое объяснение:")
print("1. Разделение:")
print("   [-3, 5, 0] | [-8, 1, 10]")
print("2. Дальнейшее разделение:")
print("   [-3] [5, 0] | [-8] [1, 10]")
print("3. Разделение до единичных элементов:")
print("   [-3] [5] [0] | [-8] [1] [10]")
print("4. Слияние пар:")
print("   [-3] [0, 5] | [-8] [1, 10]")
print("5. Слияние отсортированных половин:")
print("   [-3, 0, 5] | [-8, 1, 10]")
print("6. Финальное слияние:")
print("   [-8, -3, 0, 1, 5, 10]")