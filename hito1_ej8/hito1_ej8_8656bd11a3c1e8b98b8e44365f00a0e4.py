#Descomponer un número
n = str(input("Ingrese un número de hasta 4 dígitos: "))
while len(n) > 4:
    print("ERROR DEBE INGRESAR HASTA 4 DÍGITOS")
    n = str(input("Ingrese un número de hasta 4 dígitos: "))

largo = len(n)
if largo == 4:
    print("Los números ordenados de menor a mayor son: " + str(n[0]) + "M + " + str(n[1]) + "C +" + str(
        n[2]) + "D + " + str(n[3]) + "U")
elif largo == 3:
    print("Los números ordenados de menor a mayor son: " + str(n[0]) + "C + " + str(
        n[1]) + "D + " + str(n[2]) + "U")
elif largo == 2:
    print("Los números ordenados de menor a mayor son: " + str(n[0]) + "D + " + str(n[1]) + "U")
else:
    print("Los números ordenados de menor a mayor son: " + str(n[0]) + "U")
     