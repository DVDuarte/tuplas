def opera(tupla):
    if tupla[0] == "SOMA":
        resultado = x + y
        return resultado
    else:
        if tupla[0] == "MULT":
            resultado = x * y
            return resultado
        else:
            if tupla[0] == "DIV":
                resultado = x / y
                return resultado
            else:
                if tupla[0] == "SUB":
                    resultado = x - y
                    return resultado

operacao = input("Digite o código referente a operação desejada: 'SOMA', 'MULT', 'DIV' ou 'SUB': ")
x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
tupla = (operacao, x, y)

print(opera(tupla))