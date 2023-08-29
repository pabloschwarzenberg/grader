#Entrada
rut = input("Ingrese su rut[Sin DV]: ")

#Desarrollo

i = 0 
lista = []
serie = [2 , 3 , 4 , 5 , 6 , 7 , 2 , 3 , 4 , 5 , 6 , 7]

while i < len(rut):
    lista.append(int(rut[i]))
    i += 1

i = 0
mult = 0

while i < len(rut):
    mult = mult + serie[i] * lista[len(rut)-i-1]
    i += 1

A = 11 - (mult % 11)

if A == 11:
    dv = "0"
elif A == 10:
    dv = "K"
else:
    dv = str(A)
print("dv="+dv)