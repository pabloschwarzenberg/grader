numero=str(input("numero a descomponer:"))
longitud=len(numero)
if longitud==1:
 print(int(numero),"U")
if longitud==2:
 print(int(numero[0:1]),"D+",int(numero[1:]),"U")
if longitud==3:
 print(int(numero[0:1]),"C+",int(numero[1:2]),"D+",int(numero[2:]),"U")
if longitud==4:
 print(int(numero[0:1]),"M+",int(numero[1:2]),"C+",int(numero[2:3]),"D+",int(numero[3:]),"U")    