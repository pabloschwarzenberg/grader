#Cálculo del dígito verificador de un rut
#Entrada
RUT = int(input("Ingrese tu RUT: "))

Numero1 = RUT % 10
RUT = RUT // 10

Numero2 = RUT % 10
RUT = RUT // 10

Numero3 = RUT % 10
RUT = RUT // 10

Numero4 = RUT % 10
RUT = RUT // 10

Numero5 = RUT % 10
RUT = RUT // 10

Numero6 = RUT % 10
RUT = RUT // 10

Numero7 = RUT % 10
RUT = RUT // 10

Numero8 = RUT % 10
RUT = RUT // 10

Numero9 = RUT % 10

sumaTotal = (Numero1 * 2) + (Numero2 * 3) + (Numero3 * 4) + (Numero4 * 5) + (Numero5 * 6) + (Numero6 * 7) + (Numero7 * 2) + (Numero8 * 3)

resto = sumaTotal % 11

resultado = 11 - resto

if resultado == 11:
    print("dv = 0")
elif resultado == 10:
    print("dv = k")
elif resultado != 10 and resultado != 11:
    print("dv = ",resultado)