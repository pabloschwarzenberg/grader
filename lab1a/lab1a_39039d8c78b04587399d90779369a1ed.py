a= int(input("cantidad de votos comuna 1: "))
b= int(input("cantidad de votos comuna 2: "))
c= int(input("cantidad de votos comuna 3: "))
d= int(input("cantidad de votos de candidata en comuna 1: "))
e= int(input("cantidad de votos de candidata en comuna 2: "))
f= int(input("cantidad de votos de candidata en comuna 3: "))
g= a+b+c
h= d+e+f
    
if int((d*100)/a>=80):
  print("senadora electa")
elif int((e*100)/b>=80):
  print("senadora electa")
elif int((f*100)/c>=80):
  print("senadora electa")
elif int((d+e)>=70*(g/100)):
  print("senadora electa")
elif int((d+f)>=70*(g/100)):
  print("senadora electa")
elif int((f+e)>=70*(g/100)):
  print("senadora electa")
elif int((g/100)*40<=h):
  print("senadora electa")
elif int((d*100)/a!=1000):
  print("candidata perdedora")
      