# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна 
# их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму загаданных Петей чисел: "))
p = int(input("Введите произведение загаданных Петей чисел: "))

x = None
y = None

for x in range(1,1001): # делаем цикл в цикле потому что нам надо получить значения которые одновременно суммируются и умножатся друг на друга
  for y in range(1,1001):
    if s == x + y and p == x * y:
      print(f"Заданные числа {x} и {y} ")
      break # так как мы уже нашли нужные числа необходимости дальше прогонять цикл
   # else:
      #print("У заданных значений нет общих чисел которые можно сложить или умножить") #если запустить код со сточкой 17 и 18 он улетает в бесконечный цикл
      
    