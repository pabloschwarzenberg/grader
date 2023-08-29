#votos totales 
a=int(input('ingrese cantidad de votos'))
b=int(input('ingrese cantidad de votos'))
c=int(input('ingrese cantidad de votos'))
#votos para Isabel
d=int(input('ingrese cantidad de votos'))
e=int(input('ingrese cantidad de votos'))
f=int(input('ingrese cantidad de votos'))

p=(a+b+c) #total de votos
l=(d+e+f) #total de votos para Isabel
k=False 
#condicion 1
if (d+e)/p >=0.7:
    k= True
    print("electa")

if (d+f)/p >=0.7:
    k=True 
    print("electa")

if (e+f)/p >=0.7:
    k=True
    print("electa")

#condicion 2
if d/a >=0.8:
    k= True
    print("electa en la comuna 1")
if e/b >=0.8:
    k=True
    print("electa en la comuna 2")
if f/c >=0.8:
    k=True
    print("electa en la comuna 3")

#condicion 3
if (d+e+f)/p >=0.4:
    k=True
    print("electa")

if k==False:
    print("candidata perdedora")

