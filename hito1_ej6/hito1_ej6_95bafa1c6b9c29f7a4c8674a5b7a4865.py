#Ordenar tres números
 
a = int(input ("Ingrese primer número:",))
b = int(input ("Ingrese segundo número:",))
c = int(input ("Ingrese tercer  número:",))

 
if (a<=b and b<=c):
   print("{},{},{}".format(a,b,c))


elif(b<=a and a<=c):
    print("{},{},{}".format(b,a,c))


elif(c<=a and a<=b):
    print("{},{},{}".format(c,a,b))


elif(c<=a and a>=b):
    print("{},{},{}".format(c,b,a))
