#Ordenar tres numeros 
a=int(input("ingrese un valor")) 
b=int(input("ingrese un valor"))
c=int(input("ingrese un valor"))
if a<=b and b<=c:
  print("{},{},{}".format(a,b,c))
elif a<=c and c<=b:
  print("{},{},{}".format(a,c,b))
elif b<=a and a<=c:
  print("{},{},{}".format(b,a,c))
elif b<=c and c<=a:
  print("{},{},{}".format(b,c,a))
elif c<=a and a<=b:
  print("{},{},{}".format(c,a,b))
elif c<=b and b<=a:
  print("{},{},{}".format(c,b,a))

