#Suma de los N primeros números
contador=0
numero=int(input('ingrese un numero: '))
for x in range (0,numero+1):
    contador+=x
   
print(contador)