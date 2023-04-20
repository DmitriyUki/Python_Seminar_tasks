# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

n = int(input("Величина списка: ")) # запрашиваем у пользователя величину списка
n_digits = [int(input("Введите числа: ")) for i in range(n)] # через генератор списков (так называется эта строка) создаем список
print(n_digits) # печатаем получившийся список на экран
n_digits = set(n_digits) # переопеделяем список на множество используя элементы списка, для того чтобы определить уникальность элементов
print(n_digits) # выводим на экран вновь созданное множество
print(len(n_digits)) # считаем с помощью len колличество элементов во множестве