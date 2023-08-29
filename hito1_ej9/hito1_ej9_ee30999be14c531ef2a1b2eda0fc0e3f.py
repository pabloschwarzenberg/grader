#Sistema de Ecuaciones
def respuestaSis(x1,y1,c1,x2,y2,c2):
  determinante= x1*y2-y1*x2
  if determinante!=0:
    X=(c1*y2 - y1*c2)/ determinante
    Y=(x1*c2 - c1*x2)/ determinante
    return (X,Y)
  else:
    return ("NO HAY", "NO HAY")
x1=float(input())
y1=float(input())
c1=float(input())
x2=float(input())
y2=float(input())
c2=float(input())
respuesta=respuestaSis(x1,y1,c1,x2,y2,c2)
indice=0
lista=[]
for numero in respuesta:
  if indice==0:
    print("x=",end="")
  else:
    print("y=",end="")
  print(numero)
  indice+=1