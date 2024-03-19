import re


with open('text.txt') as f:
    data = f.read()

print('Найдите все натуральные числа (возможно, окружённые буквами)')
print(re.findall(r'[0-9]+', data))

print('Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв);')
print(re.findall(r"[А-Я]\w+", data))

print('Найдите слова, в которых есть русская буква, а за ней цифра;')
print(re.findall(r"[[а-яА-ЯёЁ]\d\w*", data))

print('Найдите все слова, начинающиеся с русской или латинской большой буквы (\b — граница слова);')
print(re.findall(r"\b[А-ЯЁA-Z]\w*", data))

print('Найдите слова, которые начинаются на гласную (\b — граница слова);')
print(re.findall(r"[аоуэыяёюеиАОУЭЫЯЁЮЕИ]\w*", data))

print('Найдите все натуральные числа, не находящиеся на границе слова;')
print(re.findall(r"\b[A-zА-я=\"#]+(\d{2,})[A-zА-я\"]+", data))

print('Найдите строчки, в которых есть символ * (. — это точно не конец строки!)')
print(re.findall(, data))
'''
print('Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки')
print(re.findall(, data))

print('Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами)')
print(re.findall(, data))

print('Выделите одним махом только текстовую часть оглавления, без тегов')
print(re.findall(, data))

print('Найдите пустые строчки')
print(re.findall(, data))

print('Найти все теги, не включая их содержимое.')
print(re.findall(, data))
'''''