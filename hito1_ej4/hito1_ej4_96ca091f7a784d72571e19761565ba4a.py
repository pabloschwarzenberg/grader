x=int(input("ingrese num"))
y=str(x)
m=0
contador=0
while x!=0:
  if x%2==1:
    m+=1*(10**contador)
  x=round(x/2)
  contador+=1
print("resultado=",m)