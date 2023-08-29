
#votos totales de cada comunas
a=float(input("ingrese numero")) 
b=float(input("ingrese numero"))
c=float(input("ingrese numero"))
#votos que obtuvo isabel por cada comuna
d=float(input("ingrese numero"))
e=float(input("ingrese numero"))
f=float(input("ingrese numero"))

t=(a+b+c) #total de votos comunal
gano=False
#pregunta a
p1=(d/a)
if p1>=0.8:
  print("senadora electa")
  gano=True
  
p2=(e/b)
if p2>=0.8:
  print("senadora electa")
  gano=True

p3=(f/c)
if p3>=0.8:
  print("senadora electa")
  gano=True

#pregunta b
p4=(d+e)/t #prueba cuatro del 70%
if p4>=0.7:
  print("senadora electa")
  gano=True

p5=(e+f)/t #prueba cinco del 70%
if p5>=0.7:
  print("senadora electa")
  gano=True

p6=(d+f)/t #prueba seis del 70%
if p6>=0.7:
  print("senadora electa")
  gano=True

#pregunta c
p7=(d+e+f)/t
if p7>=0.4:
  print("senadora electa")
  gano=True


if gano==False:
   print("cadidata perdedora")
   
