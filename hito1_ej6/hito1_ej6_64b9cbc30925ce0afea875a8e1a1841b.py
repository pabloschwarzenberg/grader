#Ordenar tres números
a=int(input("1"))
b=int(input("2"))
c=int(input("3"))
if a>=b>=c:
  print(a,",",b,",",c)
elif a>=c>=b:
  print(a,",",c,",",b)
elif b>=c>=a:
  print(b,",",c,",",a)
elif b>=a>=c:
  print(b,",",a,",",c)
elif c>=a>=b:
  print(c,",",a,",",b)
else:
  print(c,",",b,",",a)



  