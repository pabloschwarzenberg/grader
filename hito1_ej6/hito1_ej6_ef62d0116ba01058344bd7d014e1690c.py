#programa para ordenar tres numeros
#Ingreso de Datos
a=int(input("Ingrese el 1° Numero: "))
b=int(input("Ingrese el 2° Numero: "))
c=int(input("Ingrese el 3° Numero: "))

#Desarrollo del programa y su respuesta

if a<=b<=c:
    print("El orden es: " , a , "," , b , "," , c )
if b<=a<=c:
    print("El orden es: " , b , "," , a , "," , c )
if c<=a<=b:
    print("El orden es: " , c , "," , a , "," , b )
if a<=c<=b:
    print("El orden es: " , a , "," , c , "," , b )
if b<=c<=a:
    print("El orden es: " , b , "," , c , "," , a )

