def verificarTupla(tupla):
    if tupla[0] == tupla[-1]:
        return True
    else:
        return False

tamanho = int(input("Quantos elementos terá a Tupla?: "))
tupla = tamanho * [0]
for i in range(tamanho):
    tupla[i] = int(input(f"Digite o {i+1}º elemento da tupla: "))
tupla = tuple(tupla)

print(verificarTupla(tupla))