#Descomponer un número
numero = str(int(input("Ingrese un nmúero de hasta 4 dígitos: ")))
lista_num = list(numero)
contador = len(lista_num)
if(contador==4):
    Mil = lista_num[0]
    Cien = lista_num[1]
    Diez = lista_num[2]
    Uno = lista_num[3]
    print(Mil,"M",sep="",end="")
    print("","+","",end="")
    print(Cien,"C",sep="",end="")
    print("","+","",end="")
    print(Diez,"D",sep="",end="")
    print("","+","",end="")
    print(Uno,"U",sep="")
if(contador==3):
    Cien = lista_num[0]
    Diez = lista_num[1]
    Uno = lista_num[2]
    print(Cien,"C",sep="",end="")
    print("","+","",end="")
    print(Diez,"D",sep="",end="")
    print("","+","",end="")
    print(Uno,"U",sep="")
if(contador==2):
    Diez = lista_num[0]
    Uno = lista_num[1]
    print(Diez,"D",sep="",end="")
    print("","+","",end="")
    print(Uno,"U",sep="")
if(contador==1):
    Uno = lista_num[0]
    print(Uno,"U",sep="")