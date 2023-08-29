#Cálculo del dígito verificador de un rut

rut = input()
largo = len(str(rut))
numero = int((23456723 - (23456723 % (10**(8-largo))))/(10**(8-largo)))
numero_para_usar = (str(numero)[::-1])

i = int(0)
suma = int(0)

while i < largo:
    suma = suma + (int(rut[i]) * int(numero_para_usar[i]))
    i = i + 1

resto = suma % 11
resultado = 11-resto

if resultado == 10:
    print("dv=k")
elif resultado == 11:
    print("dv=0")
else:
    print("dv=",resultado)
