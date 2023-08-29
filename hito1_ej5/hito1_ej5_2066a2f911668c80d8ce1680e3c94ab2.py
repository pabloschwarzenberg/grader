#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese RUT: "))
rut_invertido = rut[::-1]

numeros = [2, 3, 4, 5, 6, 7]
suma = 0
for i in range(len(rut_invertido)):
    suma += int(rut_invertido[i]) * numeros[i % len(numeros)]

resto_num = suma % 11
digito = 11 - resto_num

if digito == 11:
    digito = 0
elif digito == 10:
    digito = "K"

print("dv =", digito)      