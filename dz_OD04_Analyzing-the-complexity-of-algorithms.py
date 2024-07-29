def optimized_merge_sort(arr):
    # Функция сортировки вставками для малых подмассивов
    def insertion_sort(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            # Сдвигаем элементы больше key вправо
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    # Основная рекурсивная функция сортировки слиянием
    def merge_sort_hybrid(arr, left, right):
        # Оптимизация 1: Используем сортировку вставками для малых подмассивов
        if right - left <= 10:
            insertion_sort(arr, left, right)
            return

        mid = (left + right) // 2

        # Рекурсивно сортируем левую и правую половины
        merge_sort_hybrid(arr, left, mid)
        merge_sort_hybrid(arr, mid + 1, right)

        # Оптимизация 2: Проверяем, нужно ли слияние
        if arr[mid] <= arr[mid + 1]:
            return  # Массивы уже отсортированы относительно друг друга

        # Слияние отсортированных половин
        merge(arr, left, mid, right)

    # Функция слияния двух отсортированных подмассивов
    def merge(arr, left, mid, right):
        # Создаем временные подмассивы
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]

        i, j, k = 0, 0, left

        # Сравниваем и объединяем элементы из двух подмассивов
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы из левого подмассива, если они есть
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Добавляем оставшиеся элементы из правого подмассива, если они есть
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    # Запускаем сортировку
    merge_sort_hybrid(arr, 0, len(arr) - 1)


# Тестирование алгоритма
if __name__ == "__main__":
    # Создаем тестовый массив
    test_arr = [-3, 5, 0, -8, 1, 10, 7, -2, 3, 4, 6, 9]
    print("Исходный массив:", test_arr)

    # Применяем оптимизированную сортировку слиянием
    optimized_merge_sort(test_arr)
    print("Отсортированный массив:", test_arr)

    # Пояснение оптимизаций:
    print("\nПрименённые оптимизации:")
    print("1. Гибридный подход: Использование сортировки вставками для малых подмассивов (≤10 элементов).")
    print(
        "2. Проверка необходимости слияния: Если последний элемент левой половины ≤ первого элемента правой половины, слияние пропускается.")
    print(
        "3. Улучшение локальности данных: Работа с подмассивами через индексы вместо создания новых массивов на каждом шаге рекурсии.")