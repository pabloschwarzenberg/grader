genoma=input("ingrese secuencia:")
a=genoma.find("a")
c=genoma.find("c")
t=genoma.find("t")
g=genoma.find("g")

if 1<=len(genoma)<=4 and a>=0 and c>=0 and t>=0 and g>=0:
  print("secuencia correcta")
else:
  print("secuencia incorrecta")