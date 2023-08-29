#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos:"))
w=((numero//1000)%10)
x=((numero//100)%10)
y=((numero//10)%10)
z=((numero//1)%10)
if numero>=0 and numero<=9:
    print(z, "U")
elif numero>=10 and numero<=99:
    print(y, "D+",z,"U")
elif numero>=100 and numero<=999:
    print(x,"C+",y,"D+",z,"U")
elif numero>=1000 and numero<=9999:
    print(w,"M+",x,"C+",y,"D+",z,"U")







