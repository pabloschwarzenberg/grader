#Descomponer un número
## ENTRADA DATOS - PROCESO -SALIDA

Número = input("Ingrese un número de hasta 4 digitos: ")

if len(Número) > 4:
    print("El número ingresado tiene más de 4 digitos")
else:
    Unidades = int(Número[-1])
    Decenas = int(Número[-2])if len(Número) >= 2 else 0
    Centenas = int(Número[-3])if len(Número)>= 3 else 0
    Miles = int(Número[-4])if len(Número) >= 4 else 0

print(Miles,"M", "+", Centenas,"C", "+", Decenas,"D", "+", Unidades,"U")