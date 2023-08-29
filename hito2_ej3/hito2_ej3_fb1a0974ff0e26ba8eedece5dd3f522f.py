string = str(input("Cadena:"))
n = int(input("n ="))
contador = 0
string = string.strip()
lista = []


for i in range(len(string) - n +1):
    lista.append(string[i:i+n])
for j in lista:
    if lista.count(j) == 1:
        print(j)
        contador += 1
if contador == 0:
    print("ninguna")
    