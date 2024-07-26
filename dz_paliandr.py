# Удалить все пробелы и знаки препинания из строки.
# Привести все символы в строке к нижнему регистру.
# Создать новую строку, которая является обратной копией исходной строки.
# Сравнить исходную строку с обратной.
# Если строки идентичны, то исходная строка является палиндромом.
# Если строки различаются, то исходная строка не является палиндромом.

import re

def is_palindrome(string):
    # Шаг 1: Удаление пробелов и знаков препинания
    cleaned_string = re.sub(r'[^\w]', '', string)

    # Шаг 2: Приведение к нижнему регистру
    cleaned_string = cleaned_string.lower()

    # Шаг 3 и 4: Создание обратной строки и сравнение
    return cleaned_string == cleaned_string[::-1]

# Примеры использования:
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Level"))  # False
print(is_palindrome("Аргентина манит негра"))  # True
print(is_palindrome("Привет, мир!"))  # False