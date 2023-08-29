valor_1 = input("cadena 1: ")
valor_2 = input("cadena 2: ")
lista2=[]
for i in valor_2:
    lista2.append(i)

lista_Alineada = []
for i in range(len(valor_1)):
    lista_Alineada.append("_")
inicio = 0

while len(lista2) > 0:
    for i in range(inicio,len(valor_1)):
        if inicio+1 == len(valor_1):
            sobrante = len(lista2)
            lista2=[]
        if len(lista2) == 0 :
            break
        if lista2[0] == valor_1[i]:
            inicio = i
            lista_Alineada[i] = lista2[0]
            lista2.pop(0)

resto = valor_2[len(valor_2)-sobrante:]
palabra =""
for x in lista_Alineada:
    palabra+=x
palabra+=resto
print(palabra)