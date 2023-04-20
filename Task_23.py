# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

list_1 = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(list_1)):
    if list_1[i-1] < list_1[i]:
        count += 1
print(count)