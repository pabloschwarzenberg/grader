#Pedimos al usuario que ingrese un número natural
print("Ingrese un número natural: ")
num=int(input())

#creamos la operación
suma=num*(num+1)/2

#creamos las condiciones y luego imprimimos
if num>0:
    print("La suma de los",num,"primeros números es igual a: ",suma)

else:
    print("Debes ingresar un número entero positvo.")      