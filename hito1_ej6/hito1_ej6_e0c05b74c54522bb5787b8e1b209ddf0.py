#Ordenar tres números
a=int(input())   
b=int(input())
c=int(input())

if a>=b and a>=c and b>=c:
  print(c,",",b,",",a)
if b>=a and a>=c and b>=c:
  print(c,",",a,",",b)
if a>=b and c>=b and a>=c:
  print(b,",",c,",",a)
if b>=a and b>=c and c>=a:
  print(a,",",c,",",b)
if c>=a and c>=b and b>=a:
  print(a,",",b,",",c)
if c>=a and c>=b and a>=b:
  print(b,",",a,",",c)
 
  