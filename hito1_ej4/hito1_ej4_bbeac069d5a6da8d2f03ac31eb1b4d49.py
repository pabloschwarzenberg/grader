#Entrada
Num = int(input("Ingrese un numero a transformar a binario: "))

lista = []
inv = ""

#Desarrollo
while Num != 0:
    Bin = Num % 2
    Num //= 2
    lista.append(Bin)

for i in reversed(lista):
    inv = inv + str(i)
print("resultado=",inv)