#Descomponer un número

num=int(input("ingrese un numero de hasta 4 digitos :"))
a=len(str(num))
while not a<=4:
    num=int(input("ingrese un numero de 4 digitos"))

unidad = num%10
decena=num%100
centena=num%1000
mil=num%10000

U=unidad//1
D=decena//10
C=centena//100
M=mil//1000

if a==4:
    print(M,"M" ,"+" ,C,"C", "+" ,D,"D" ,"+",U, "U")
elif  a==3:
     print(C,"C", "+" ,D,"D" ,"+",U, "U")
elif  a==2:
    print(D,"D" ,"+",U, "U")
elif  a==1:
    print(U, "U")

    