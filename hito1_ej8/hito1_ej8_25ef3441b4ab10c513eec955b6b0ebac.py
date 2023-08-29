#Descomponer un número
numero=str(input("Ingrese un número del 1 a 4 dígitos: "))
digito=len(numero)
if digito==1:
    print(numero[0]+"U")
if digito==2:
    print(numero[0]+"D","+",numero[1]+"U")
if digito==3:
    print(numero[0]+"C","+",numero[1]+"D","+",numero[2]+"U")
if digito==4:
    print(numero[0]+"M","+",numero[1]+"C","+",numero[2]+"D","+",numero[3]+"U")