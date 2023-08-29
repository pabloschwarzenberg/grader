#Descomponer un número
n = int(input("ingrese un numero de hasta 4 digitos: "))

d1= n//1000
d2 = n //100 % 10
d3 = n //10 % 10
d4 = n % 10

d1 = str(d1)
d2 = str(d2)
d3 = str(d3)
d4 = str(d4)
r1 = d1+"M"
r2 = d2+"C"
r3 = d3+"D"
r4 = d4+"U"


if n>999 and n<=9999:
    print(r1,"+",r2,"+",r3,"+",r4)
elif n <= 999 and n > 99:
    print(r2,"+",r3,"+",r4)
elif n <= 99 and n > 9:
    print(r3,"+",r4)
elif n <= 9 and n >= 0:
     print(r4)
else:
    if n >9999:
        print("numero no valido")
