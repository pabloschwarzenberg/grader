a=int(input("ingrese el primer numero"))
b=int(input("ingrese el segundo numero"))
c=int(input("ingrese el tercer numero"))
if(a >=b >=c):
   print(c, ",", b, ",", a)
elif(a >=c >=b):
   print(b, ",", c, ",", a)
elif(c >=b >=a):
   print(a, ",", b, ",", c)
elif(c >=a >=b):
   print(b, ",", a, ",", c)
elif(b >=c >=a):
   print(a, ",", c, ",", b)
elif(b >=a >=c):
   print(c, ",", a, ",", b)