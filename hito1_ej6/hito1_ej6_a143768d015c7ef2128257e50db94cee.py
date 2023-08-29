a = int(input("ingrese un numero "))
b = int(input("ingrese un numero "))
c = int(input("ingrese un numero "))
if a < b and a<c:
    print ("el mayor es",a)
if b < a and b <c:
    print ("el mayor es",b)
if c < a and c <b:
    print ("el mayor es",c)
if a > b and a>c:
    print ("el menor es ",a)
if b > a and b>c:
    print ("el menor es",b)
if c > a and c>b:
    print ("el menor es",c)