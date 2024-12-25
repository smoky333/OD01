# 1. Приводим строку к нижнему регистру для игнорирования разницы между прописными и строчными буквами
# 2. Удаляем все символы, кроме букв и цифр, с помощью генератора
# 3. Сравниваем отфильтрованную строку с её обратной версией





def is_palindrome(s):

    s = s.lower()
    s = ''.join(c for c in s if c.isalnum())

    return s == s[::-1]



example = "А роза упала на лапу Азора"
example1 = "Новости"
example2 = "12321"
print(is_palindrome(example))  # True
print(is_palindrome(example1))  # False
print(is_palindrome(example2))  # True

