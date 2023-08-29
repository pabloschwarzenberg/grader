a=int(input("escribe un numero"))
b=int(input("escribe otro numero"))
c=int(input("escribe otro numero"))
if a <= b <= c:
  print(a,",",b,",",c)
elif a <= c <= b:
  print(a,",",c,",",b)
elif b <= a <= c:
  print(b,",",a,",",c)
elif b <= a <= c:
  print(b,",",a,",",c)
elif c <= a <= b:
  print(c,",",a,",",b)
elif c <= b <= a:
  print(c,",",b,",",a)