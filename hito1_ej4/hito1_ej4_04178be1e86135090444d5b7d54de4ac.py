decimal = int(input())
lista_modulos = []
while decimal != 0:
    modulo = decimal % 2
    cociente = decimal // 2
    #print("COCIENTE::: " + str(cociente))
    lista_modulos.append(str(modulo))
    decimal = cociente
print("resultado=" + "".join(lista_modulos[::-1]))