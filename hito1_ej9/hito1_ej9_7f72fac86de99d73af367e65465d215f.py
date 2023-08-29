#Sistema de Ecuaciones
a=input("ingrese numero: ")
b=input("ingrese numero: ")
c=input("ingrese numero: ")
d=input("ingrese numero: ")
e=input("ingrese numero: ")
f=input("ingrese numero: ")
xdea=int(a)
ydea=int(b)
resultadoa=int(c)
xdeb=int(d)
ydeb=int(e)
resultadob=int(f)
y=1
ypos=1
yneg=-1
ycorrecta=False
while ycorrecta==False:
  if (resultadoa-ydea*ypos)/xdea==(resultadob-ydeb*ypos)/xdeb:
    y=ypos
    ycorrecta=True
  if (resultadoa-ydea*yneg)/xdea==(resultadob-ydeb*yneg)/xdeb:
    y=yneg
    ycorrecta=True
  else:
    ypos+=1
    yneg-=1

x=1
xpos=1
xneg=-1
xcorrecta=False
while xcorrecta==False:
  if xdea*xpos+ydea*y==resultadoa:
    x=xpos
    xcorrecta=True
  if xdea*xneg+ydea*y==resultadoa:
    x=xneg
    xcorrecta=True
  else:
    xpos=xpos+1
    xneg=xneg-1
    
x=float(x)
y=float(y)
print("x="+str(x)+", "+"y="+str(y))
