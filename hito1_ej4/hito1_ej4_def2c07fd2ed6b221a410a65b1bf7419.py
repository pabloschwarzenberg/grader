#Conversión de Decimal a Binario
x=int(input("Ingrese un numero: "))
i=0
d=0
r=0
l=[]
w=0
while i<1:
     if x<1:
               l.append(0)
     if d<1: 
          y=x//2
          z=x%2
          l.append(z)
          d=d+1
     if r<1:
          z=y%2
          l.append(z)
          r=r+1
     y=y//2
     z=y%2
     l.append(z)
     if y<=1:
          if z==1:
               break 
t=len(l)
while t>0:
     if w<1:
          print("resultado=",end="")
          w=w+1
     print(l[t-1],end="")
     t=t-1