def intercala(tupla1, tupla2):
    tuplaIntercalada = (tupla1[0], tupla2[0], tupla1[1], tupla2[1], tupla1[2], tupla2[2])
    return tuplaIntercalada


a = int(input("Digite o primeiro elemento da tupla 1: "))
b = int(input("Digite o segundo elemento da tupla 1: "))
c = int(input("Digite o terceiro elemento da tupla 1: "))
tupla1 = (a, b, c)

x = int(input("Digite o primeiro elemento da tupla 2: "))
y = int(input("Digite o segundo elemento da tupla 2: "))
z = int(input("Digite o terceiro elemento da tupla 2: "))
tupla2 = (x, y, z)


print(intercala(tupla1, tupla2))