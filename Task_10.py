# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

import random # даная команда всегда идет вверху

n = int(input("Введите колличество монеток: "))

gerb = 0
reska = 0
temps = []

for i in range(n):                 # range означает что программа пройдется по всем числам корые ввел пользователь в переменной n
  temp = random.randint(0, 1)      #создаем рандомом интовое число, можно создать элемент любого типа
  temps.append(temp)               # добавляем полученные значения в список за пределами цикла 
print(temps)                       # выводим список на печать      

for j in temps:
 if j > 0:
   gerb += 1

for p in temps:
  if p == 0:
    reska += 1

if gerb > reska:
  print(f"Минимальное колличество монеток, которые необходимо перевернуть - {reska} ")

else: 
  print(f"Минимальное колличество монеток, которые необходимо перевернуть - {gerb} ")

                                  