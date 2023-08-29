rut=int(input("ingrese rut sin puntos, guión ni DV"))
x=0
y=2
while rut>0:
  z=int(rut%10)
  x=x+(z*y)
  if y==7:
    y=2
  else:
    y=y+1
  rut=int(rut/10)
resto=x%11
DV=11-resto
if DV==10:
  DV="K"
elif DV==11:
  DV=0
print("dv=",DV) 