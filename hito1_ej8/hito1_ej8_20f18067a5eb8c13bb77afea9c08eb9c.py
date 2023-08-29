#Descomponer un número
a=int(input("Ingrese un numero de 4 digitos:"))
while a>10000:
      a=int(input("Ingrese un numero de 4 digitos:"))
b=str(a)
if a>1000:
    print(b[0:1],"M+",b[1:2],"C+",b[2:3],"D+",b[3:],"U")
elif a>100:
    print(b[0:1],"C+",b[1:2],"D+",b[2:],"U")
elif a>10:
    print(b[0:1],"D+",b[1:],"U")
elif a>=1:
    print(b[1:],"U")
        