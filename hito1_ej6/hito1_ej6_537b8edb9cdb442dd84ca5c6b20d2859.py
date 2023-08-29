a=input("ingrese a: ")
int(a)
b=input("ingrese b: ")
int(b)
c=input("ingrese c: ")
int(c)
if a>=b and b>=c:
  print(c+","+b+","+a)
if b>=a and a>=c:
  print(c+","+a+","+b)
if c>=b and b>=a:
  print(a+","+b+","+c)
if c>=b and b>=a:
  print(a+","+b+","+c)
if a>=c and c>=b:
  print(b+","+c+","+a)
if c>=a and a>=b:
  print(b+","+a+","+c)
