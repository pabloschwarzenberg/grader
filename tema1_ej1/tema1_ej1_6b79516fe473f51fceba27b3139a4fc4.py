#Suma de los N primeros números
#Guardar variable
numeros = eval(input("Ingrese cantidad de numeros naturales: "))
#Calcular suma y mostrar resultado
if (numeros > 0):
   suma = numeros+1
   multi = suma*numeros
   division = multi/2
   print("La suma es",int(division))

else:
    print("No se puede realizar la suma")     