numero=int(input())
resto=[]
while numero>0:
  r=numero%2
  resto.append(str(r))
  numero=numero//2
resto.reverse()
respuesta="".join(resto)
respuesta=int(respuesta)
print("resultado=",respuesta)
