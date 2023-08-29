#Ordenar tres números
a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
c=int(input("Ingrese c: "))
if a<=b<=c: 
   print(a,",",b,",",c)
elif c<=a<=b: 
   print(c,",",a,",",b)
elif b<=c<=a: 
   print(b,",",c,",",a)
elif a<=c<=b: 
   print(a,",",c,",",b)
elif c<=b<=a: 
   print(c,",",b,",",a)
elif b<=a<=c: 
   print(b,",",a,",",c)