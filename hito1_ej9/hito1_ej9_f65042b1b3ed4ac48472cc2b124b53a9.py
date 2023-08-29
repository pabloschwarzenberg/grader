#los coeficientes a,b,c son para la primera ecuación,y los coeficientes d,e,f son para la segunda ecuación
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())

dd=a*e-b*d

if dd!=0:
  x=(e*c-b*f)/dd
  y=(a*f-d*c)/dd
  print("x=",x,"y=",y)