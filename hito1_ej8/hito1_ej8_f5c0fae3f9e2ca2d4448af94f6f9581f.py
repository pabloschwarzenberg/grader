#ENTRADA
num = input("Ingrese un número de 4 dígitos como máximo: ")

#SALIDA
if len(num) == 4:
    print(str(num[0]) + "M" + " + " + str(num[1]) + "C" + " + " + str(num[2]) + "D" + " + " + str(num[3]) + "U")
    
elif len(num) == 3:
    print(str(num[0]) + "C" + " + " + str(num[1]) + "D" + " + " + str(num[2]) + "U")

elif len(num) == 2:
    print(str(num[0]) + "D" + " + " + str(num[1]) + "U")

elif len(num) == 1:
    print(str(num[0]) + "U")

else:
    print("No ingreso un número correcto")


