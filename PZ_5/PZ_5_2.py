#2. Описать функцию AddRightDigit(D, K), добавляющую к целому положительному
#числу K справа цифру D (D — входной параметр целого типа, лежащий в диапазоне
#0-9, K — параметр целого типа, являющийся одновременно входным и выходным).
#С помощью этой функции последовательно добавить к данному числу K справа
#данные цифры D1 и D2, выводя результат каждого добавления.
K=int(input("Введите число "))
D1=int(input("Введите цифру "))
D2=int(input("Введите число "))
def AddRightDigit(D, K):
    K = K*10+D
    result = K
    return result

K = AddRightDigit(D1,K)
print("Результат добавления D1",K)

K = AddRightDigit(D2,K)
print("Результат добавления D2",K)