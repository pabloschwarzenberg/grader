a=int(input("ingrese el numero total de votantes en la comuna uno: "))
b=int(input("ingrese el numero total de votantes en la comuna dos: "))
c=int(input("ingrese el numero total de votantes en la comuna tres: "))
d=int(input("ingrese el numero de votos de la comuna uno: "))
e=int(input("ingrese el numero de votos de la comuna dos: "))
f=int(input("ingrese el numero de votos de la comuna tres: "))
if int((d*100)/a>=80):
  print("senadora electa")
elif int((e*100)/b>=80):
  print("senadora electa")
elif int((f*100)/c>=80):
  print("senadora electa")
elif int((d+e)>=70*((a+b+c)/100)):
  print("senadora electa")
elif int((d+f)>=70*((a+b+c)/100)):
  print("senadora electa")
elif int((f+e)>=70*((a+b+c)/100)):
  print("senadora electa")
elif int(((a+b+c)/100)*40<=d+e+f):
  print("senadora electa")
elif int((d*100)/a!=1000):
  print("candidata perdedora")