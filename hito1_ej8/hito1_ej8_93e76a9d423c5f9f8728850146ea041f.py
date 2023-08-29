#Descomponer un número
n=int(input("Ingresar numero:"))
a=(n//10**3)
b=(n//10**2)%10
c=(n//10)%10
d=(n%10)
n=str(n)
digitos=len(n)
if digitos == 4:
    print(a, "M", "+", b, "C", "+", c, "D", "+", d, "U")
if digitos==3:
    print( b, "C", "+", c, "D", "+", d, "U")
if digitos==2:
    print(c, "D", "+", d, "U")
if digitos==1:
    print(d, "U")      