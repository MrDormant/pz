# Вариант 7. Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16',
# отражающая продажи продукции по дням в кг. Преобразовать информацию из
# строки в ewter словари, с использованием функции найти минимальные продажи по
# каждому виду продукции, результаты вывести на экран.

text = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
s = text.split()

sp = {}
for i in range(0,len(s),6):
    sp[s[i]] = list(map(int, s[i+1:i+6]))
print(sp)
for f in sp:
   print('самые маленикие продажи продукта ',f,':',min(sp[f]))
