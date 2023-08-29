#Descomponer un número
n=int(input("ingrese un numero de hasta 4 cifras: "))
a1=int(n/1000)
d1=a1%10
a2=int(n/100)
d2=int(a2%10)
a3=n%100
d3=int(a3/10)
d4=n%10
d1=str(d1)
x1=(d1+"M")
d2=str(d2)
x2=(d2+"C")
d3=str(d3)
x3=(d3+"D")
d4=str(d4)
x4=(d4+"U")
print(x1,"+",x2,"+",x3,"+",x4)