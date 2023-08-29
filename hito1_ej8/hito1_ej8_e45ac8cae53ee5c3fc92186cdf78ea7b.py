#Descomponer un número
n=input("ingrese el numero que desea descomponer: ")
if len(n) ==4:
     print(n[-4],"M+",n[-3],"C+",n[-2],"D+",n[-1],"U")
if len(n)== 3:
     print(n[-3],"C+",n[-2],"D+",n[-1],"U")
if len(n)== 2:
     print(n[-2],"D+",n[-1],"U")
if len(n)== 1:
     print(n[-1],"U")