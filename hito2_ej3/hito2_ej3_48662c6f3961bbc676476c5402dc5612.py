string = input()
n = int(input())

lista = []
for i in range(len(string) + 1 - n):
    palabra = ""
    for j in range(n):
        palabra += string[i + j]
    
    lista.append(palabra)

unicas = []
for e in lista:
    if lista.count(e) == 1:
        unicas.append(e)
        print(e)

if len(unicas) == 0:
    print("ninguna")