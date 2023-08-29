#Cálculo del dígito verificador de un rut

listar_digitos = []
a = 2
rut = input("numero: ")
lista_rut = []
for letra in rut:
    lista_rut.append(letra)

lista = lista_rut[::-1]
for numero in lista:
    listar_digitos.append(int(numero) * a)
    a = a + 1
    if a > 7:
        a = 2

suma = 0

for contador in listar_digitos:
    suma = contador + suma

resto = suma % 11
final = 11 - resto


if final == 11:
    print("dv= 0")
elif final == 10:
    print("dv= k")
else:
    print("dv=", final)