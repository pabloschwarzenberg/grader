rut = int(input("ingrese rut: "))
print("descomponer rut", rut//10000000)
print("descomponer rut", rut//1000000)
print("descomponer rut", rut//100000)
print("descomponer rut", rut//10000)
print("descomponer rut", rut//1000)
print("descomponer rut", rut//100)
print("descomponer rut", rut//10)
print("descomponer rut", rut//1)
a=(rut//10000000) * 3
print("resultado de a es:",a)
b=((rut//1000000)%10)*2
print("el resultado de b:", b)
c=((rut//100000)%10)*7
print("el resultado de c:",c)
d=((rut//10000)%10)*6
print("el resultado de d:",d)
e=((rut//1000)%10)*5
print("el resultado de e:",e)
f=((rut//100)%10)*4
print("el resultado de f:",f)
g=((rut//10)%10)*3
print("el resultado de g:",g)
h=((rut//1)%10)*2
print("el resultado de h:", h)
suma = (a+b+c+d+e+f+g+h)
print("resultado de la suma:",suma)
resto1 = suma//11
print("resultado de resto1=suma //11 :",resto1)
resto2 = suma-(11*resto1)
print("resultado de la resta2=suma-(11*resto1):",resto2)
resta = 11-resto2
print("resultado e la resta=11-resto2:", resta)
if (resta == 11):
    print("dv=",end="")
    print(0)
elif (resta == 10):
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)