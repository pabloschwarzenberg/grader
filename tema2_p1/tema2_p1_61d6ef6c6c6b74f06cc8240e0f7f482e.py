# por favor escribe aquí tu función
#Inicio
print("Determinar si el número es primo o compuesto")
# pedirle al usuario que ingrese un número del 2 al 10
num = int(input("Ingrese un número del 2 al 10: "))
#Proceso
if (num<2) or (num>10):
    print("El número está fuera del rango")
elif (num==2) or (num==3) or (num==5) or (num==7):
    print("El número", num,"es primo")
else:
    print("El número", num,"es compuesto")