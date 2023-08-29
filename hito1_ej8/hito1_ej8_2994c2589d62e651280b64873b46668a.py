#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 digitos:"))

contador = 1
control = 10
while control <= numero:
    contador = contador + 1
    control = control * 10
str(contador)


if int(str(contador)) == 1:
    print(numero,"U")
elif int(str(contador)) == 2:
    ultimo = numero%10
    primero = numero//10
    print(primero,"D + ",ultimo,"U")
elif int(str(contador)) == 3:
    ultimo = numero%10
    numero = numero//10
    penultimo = numero%10
    primero = numero//10
    print(primero,"C + ",penultimo,"D + ",ultimo,"U")
elif int(str(contador)) == 4:
    ultimo = numero %10
    numero = numero//10
    penultimo =  numero%10
    numero=numero//10
    antepenultimo = numero%10
    primero = numero //10
    print(primero,"M +",antepenultimo,"C + ",penultimo,"D + ",ultimo,"U")
else:
    print("")

