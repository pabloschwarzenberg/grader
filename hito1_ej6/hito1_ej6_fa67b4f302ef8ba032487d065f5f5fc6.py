#Ordenar tres números
a = int(input())
b = int(input())
c = int(input())

if c <= b <= a :
  print(c,",",b,",",a)
elif c <= a <= b :
  print(c,",",a,",",b)
elif b <= c <= a :
  print(b,",",c,",",a)
elif b <= a <= c :
  print(b,",",a,",",c)
elif a <= b <= c :
  print(a,",",b,",",c)
elif a <= c <= b :
  print(a,",",c,",",b)
      