a=input()
b=input()
c=input()
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
  if b>c:
    k=str(c)+","+str(b)+","+str(a)
  else:
    k=str(b)+","+str(c)+","+str(a)
else:
  if b>a and b>c:
    if a>c:
      k=str(c)+","+str(a)+","+str(b)
    else:
      k=str(a)+","+str(c)+","+str(b)
  else:
    if c>a and c>b:
      if a>b:
        k=str(b)+","+str(a)+","+str(c)
      else:
        k=str(a)+","+str(b)+","+str(c)
print(k)