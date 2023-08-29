#Descomponer un número
a= int(input("ingrese un numero entero para descomponerlo: "))

UNIDAD= (a%10)

a//=10

DECENA= (a%10)

a//= 10

CENTENA= (a%10)

a//=10

MIL= (a%10)


print(str(MIL)+"M" "+" + str(CENTENA)+"C" "+" + str(DECENA)+"D" "+" + str(UNIDAD)+"U")      