print("Descomponer un número")
numero=int(input("Ingrese un número de hasta 4 dígitos:"))
numeroStr=str(numero)
largo=len(numeroStr)
if largo==1:
    print(numeroStr[0]+"U")
if largo==2:
    print((numeroStr[0]+"D+")+(numeroStr[1]+"U"))
if largo==3:
    print((numeroStr[0]+"C+")+(numeroStr[1]+"D+")+(numeroStr[2]+"U"))
if largo==4:
    print((numeroStr[0]+"M+")+(numeroStr[1]+"C+")+(numeroStr[2]+"D+")+(numeroStr[3]+"U"))