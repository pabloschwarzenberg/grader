a=int(input("Escriba el primer número:"))
b=int(input("Escriba el segundo número:"))
c=int(input("Escriba el tercer número:"))
if a<=b<=c:
 print("{},{},{}".format(a,b,c))
if a<=c<=b:
 print("{},{},{}".format(a,c,b))
if b<=a<=c:
 print("{},{},{}".format(b,a,c))
if b<=c<=a:
 print("{},{},{}".format(b,c,a))
if c<=a<=b:
 print("{},{},{}".format(c,a,b))
if c<=b<=a:
 print("{},{},{}".format(c,b,a))
