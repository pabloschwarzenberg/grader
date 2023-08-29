#Contestador de celular
print("El numero debe tener 8 cifras,(por ejemplo 78735653) ")
numero= int(input("Ingrese el numero telefonico: "))
hora= int(input("Ingrese la hora de llamada: "))
primero= numero//100000
ultimo= numero%1000
while hora >0 and hora < 23:
    if hora > 0 and hora < 7:
        print("Contestar")
        hora= 0
    elif hora < 14 and not ultimo==909:
        print("No contestar")
        hora= 0
    elif hora < 14 and ultimo ==909:
        print("contestar")
        hora= 0
    elif hora > 17 and hora < 19 and not primero==877:
        print("Contestar")
        hora=0

    elif hora > 19:
        print("No contestar")
        hora= 0
    elif hora > 17 and hora < 19 and primero==877:
        print("No contestar")
        hora= 0
print("El programa ha finalizado")     