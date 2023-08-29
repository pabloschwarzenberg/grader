#Ordenar tres números
a=int(input("Primer numero  "))
b=int(input("Segundo numero  "))
c=int(input("Tercer Numero  "))
if (a<=b<=c):
    print("{},{},{}".format(a,b,c))
if b<=a<=c:
    print("{},{},{}".format(b,a,c))
if c<=a<=b:
     print("{},{},{}".format(c,a,b))
if b<=c<=a:
    print("{},{},{}".format(b,c,a))
if a<=c<=b:
    print("{},{},{}".format(a,c,b))
if c<=b<=a:
    print("{},{},{}".format(c,b,a))
 