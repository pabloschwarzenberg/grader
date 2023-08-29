#Cálculo del dígito verificador de un rut
lista2 = []
a = 2
rut = input("numero: ")
lista_rut = []
for letra in rut:
    lista_rut.append(letra)

lista = lista_rut[::-1]
for numero in lista:
    lista2.append(int(numero) * a)
    a = a + 1
    if a > 7:
        a = 2

suma = 0

for i in lista2:
    suma = i + suma

resto = suma % 11
final = 11 - resto

if final == 11:
    print("dv= 0")
elif final == 10:
    print("dv= k")
else:
    print("dv=",final)