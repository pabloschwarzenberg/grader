#Descomponer un número
n = input("Ingrese un número de hasta 4 dígitos")
if len(n) == 1:
    print(n[0:1]+"U")
if len(n) == 2:
    print(n[0:1]+"D","+",n[1:2]+"U")
if len(n) == 3:
    print(n[0:1]+"C","+",n[1:2]+"D","+",n[2:3]+"U")
if len(n) == 4:
    print(n[0:1]+"M","+",n[1:2]+"C","+",n[2:3]+"D","+",n[3:4]+"U")