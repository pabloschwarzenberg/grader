#Suma de los N primeros números
#Entrada
num=int(input("Introduzca un número natural: "))

if num>= 1 :
    suma=(num*(num + 1))/2
    print("La suma de los", num, "primeros números naturales es",int(suma))
    
else:
    print("El número introducido no corresponde a un número natural")    