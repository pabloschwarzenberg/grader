#Ordenar tres números
a=int(input("Esbribe el primer numero: "))
b=int(input("Esbribe el segundo numero: "))
c=int(input("Esbribe tercer numero: "))
if a<=b<=c:
  print(a,",",b,",",c)
elif a<=c<=b:
  print(a,",",c,",",b)
elif b<=a<=c:
  print(b,",",a,",",c)
elif b<=c<=a:
  print(b,",",c,",",a)
elif c<=a<=b:
  print(c,",",a,",",b)
elif c<=b<=a:
  print(c,",",b,",",a)