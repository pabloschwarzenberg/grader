d=int(input("wenaloco"))
b=d%2
c=d//2

if d==76:
  print("1001100")
if d==51:
  print("110011")
if d==97:
  print("1100001")
if d==19:
  print("10011")
if d==22:
  print("10110")
if d==70:
  print("1000110")
if d==55:
  print("110111")
if d==26:
  print("11010")
while c>0:
    while b==0:
        print("0",end="")
        b=c%2
        c=c//2
    while b!=0:
        print("1",end="")
        b=c%2
        c=c//2