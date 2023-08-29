#Ordenar tres números
a=int(input("wena"))
b=int(input("wenaloco"))
c=int(input("wenamaster"))
if a<=b<=c:
      print(a,",",b,",",c)
elif b<=a<=c:
      print(b,",",a,",",c)
elif c<=b<=a:
      print(c,",",b,",",a)
elif b<=c<=a:
      print(b,",",c,",",a)
elif c<=a<=b:
      print(c,",",a,",",b)

