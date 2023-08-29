numero=int(input("Ingrese un numero de 4 digitos: "))

a=(numero%10)
b=(numero%100)//10
c=((numero%1000)//100)
d=(numero%10000)//1000


print((str(d)+("M+")) + (str (c)+("C+")) + (str(b)+("D+") + (str(a) +("U"))))
