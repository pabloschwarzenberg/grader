#Contestador de celular
      import math
#Entrada.
Num = int(input("Ingrese el número de teléfono: "))
Hor = int(input("Ingrese la hora: "))
NumTerm = Num % 1000
NumEmp1 = str(Num/100000)
NumEmp2 = NumEmp1[0:4]
#Procesamiento y salida.
if 9999999 <= Num >= 99999999 and 0 <= Hor >= 23:
    if 0 <= Hor >= 7:
        print("CONTESTAR.")
    else:
        print("NO CONTESTAR.")

    if Hor < 14 and NumTerm == 909:
        print("CONTESTAR.")
    else:
        print("NO CONTESTAR.")

    if 17 <= Hor >= 19 and NumEmp2 == "877":
        print("NO CONTESTAR.")
    else:
        print("CONTESTAR.")

    if Hor > 19:
        print("NO CONTESTAR.")
