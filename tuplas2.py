def inverte(tupla):
    tuplaInvertida = (tupla[-1],tupla[-2],tupla[-3])
    return tuplaInvertida

a = int(input("Digite o primeiro elemento da tupla: "))
b = int(input("Digite o segundo elemento da tupla: "))
c = int(input("Digite o terceiro elemento da tupla: "))
tupla = (a, b, c)

print(inverte(tupla))