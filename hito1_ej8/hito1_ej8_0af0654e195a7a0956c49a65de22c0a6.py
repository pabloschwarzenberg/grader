#Descomponer un numero
numero = input("Ingrese el numero a descomponer")
n = len(numero)
if n == 4:
    print(numero[0]+"M+"+numero[1]+"C+"+numero[2]+"D+"+numero[3]+"U")
if n == 3:
    print(numero[0]+"C+"+numero[1]+"D+"+numero[2]+"U")
    
if n == 2:
    print(numero[0]+"D+"+numero[1]+"U")
if n == 1:
    print(numero+"U")
    
    