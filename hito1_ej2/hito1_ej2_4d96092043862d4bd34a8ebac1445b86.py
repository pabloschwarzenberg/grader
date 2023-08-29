a=int(input("numero telefono"))
b=int(input("hora"))
c=a%1000
d=a//100000


if b<=7:
  print("CONTESTAR")

if b<14 and b>7:
  if c == 909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
if b<=19 and b>=17:
  if d == 877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
if b>19:
  print("NO CONTESTAR")
