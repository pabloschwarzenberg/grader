#Descomponer un número
a = int(input("ingrese un nimero de hasta 4 digitos"))
unidad= a%10
print(unidad)
a//=10
decena= a%10
print(decena)
a//=10
centena=a%10
print(centena)
a//=10
mil=a%10
print(mil)
print(str(mil)+"M +", str(centena)+"C +",str(decena)+"D +",str(unidad)+"U")