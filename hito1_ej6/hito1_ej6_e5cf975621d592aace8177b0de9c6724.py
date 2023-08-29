#Ordenar tres números
a = eval(input("n1:"))
b = eval(input("n2:"))
c = eval(input("n3:"))

if a <= b and a <= c:
  if b <= c:
    print(a,",",b,",",c)
  else:
    print(a,",",c,",",b)
elif b <= a and b <= c:
  if a <= c:
    print(b,",",a,",",c)
  else:
    print(b,",",c,",",a)
elif c <= a and c <= b:
  if a <= b:
    print(c,",",a,",",b)
  else:
    print(c,",",b,",",a)