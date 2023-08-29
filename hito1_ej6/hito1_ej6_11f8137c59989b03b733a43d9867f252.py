#Ordenar tres números
print ("A continuación tendrá que darme 3 números enteros")
a=int(input("Primer número: "))
b=int(input("Segundo número: "))
c=int(input("Tercer número: "))
if a<=b<=c:
      print(str(a)+','+str(b)+','+str(c))
elif a<=c<=b:
      print(str(a)+','+str(c)+','+str(b))
elif b<=a<=c:
      print(str(b)+','+str(a)+','+str(c))
elif b<=c<=a:
      print(str(b)+','+str(c)+','+str(a))
elif c<=a<=b:
      print(str(c)+','+str(a)+','+str(b))
elif c<=b<=a:
      print(str(c)+','+str(b)+','+str(a))
