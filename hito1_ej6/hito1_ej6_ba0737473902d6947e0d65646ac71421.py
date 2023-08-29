num1=str(input("enter number"))
num2=str(input("enter number"))
num3=str(input("enter number"))

def Numbers(y,x,z):
  if x>y>z:
    print(z +", " + y +", " +x)
  if x>z>y:
      print(y + ", " + z + ", " + x)
  if y>=x>=z:
    print(z + ", " + x + ", " + y)
  if y>z>x:
    print(x + ", " + z + ", " + y)
  if z>x>y:
    print(y + ", " + x + ", " + z)
  if z>y>x:
    print(x + ", " + y + ", " + z)

def NumbersEquality(x,y,z):
  if x==z==y:
    print(z + ", " + y + ", " + x)
  if x==z>y:
    print(y + ", " + z + ", " + x)
  if x==z<y:
    print(z + ", " + x + ", " + y)
  if x==y>z:
    print(z + ", " + y + ", " + x)
  if x==y<z:
    print(x + ", " + y + ", " + z)
  if y==z>x:
    print(x + ", " + y + ", " + z)
  if y==z<x:
    print(z + ", " + y + ", " + x)

Numbers(num1,num2,num3)
NumbersEquality(num1,num2,num3)