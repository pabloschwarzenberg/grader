#Ordenar tres números
a=input("ingrese primer número: ")
b=input("ingrese segundo número: ")
c=input("ingrese tercer número: ")
if a<=b<=c or a<b<=c:
    print(a+","+b+","+c)
if a<=c<b:
    print(a+","+c+","+b)
if b<c<=a:
    print(b+","+c+","+a)
if b<=a<c:
    print(b+","+a+","+c)
if c<a<=b:
    print(c+","+a+","+b)
if c<=b<a:
    print(c+","+b+","+a)
