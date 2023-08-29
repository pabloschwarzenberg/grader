numero = int(input("ingrese numero a convertir: "))

lista = list()
while numero>0:
    numero_entero = numero//2
    resto = numero%2
    lista.append(resto)
    numero = numero//2
i = 0
lista_reversa = ["resultado="]
while len(lista)>i:
    S = lista[::-1]
    lista_reversa.append(S[i])
    i += 1
i = 0
while len(lista_reversa)>i:
    print(lista_reversa[i],end = "")
    i += 1