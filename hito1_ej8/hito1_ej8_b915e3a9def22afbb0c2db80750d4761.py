#Descomponer un número
num=input("ingrese un numero: ")
a=len(num)

if a==4:
    print(num[0:1],"M","+",num[1:2],"C","+",num[2:3],"D","+",num[3:4],"U")

if a==3:
    print(num[0:1],"C","+",num[1:2],"D","+",num[2:3],"U")

if a==2:
    print(num[0:1],"D","+",num[1:2],"U")

if a==1:
    print(num[0:1],"U")     