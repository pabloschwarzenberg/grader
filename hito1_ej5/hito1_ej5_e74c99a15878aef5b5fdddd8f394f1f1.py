n=input("Ingrese RUT:")
l=len(n)
p=0
d=0
while p<=(l-1):
  if p<=5:
    d=d+(int(n[l-1-p]))*(p+2)
    p=p+1
  else:
    d=d+(int(n[l-1-p]))*(p-4)
    p=p+1
dv=11-(d%11)
if dv==11:
  print("dv=0")
elif dv==10:
  print("dv=K")
else:
  print("dv=",dv)

