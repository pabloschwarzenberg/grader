#Ordenar tres 
nros = []
nros.append(int(input()))
segundo = int(input())
if segundo > nros[0]:
    nros.append(segundo)
else:
    nros.insert(0, segundo)
tercero = int(input())
if tercero > nros[0] and tercero > nros[1]:
  nros.append(tercero)
elif tercero > nros[0] and tercero < nros[1]:
  nros.insert(1,tercero)
else:
  nros.insert(0,tercero)
print(str(nros[0])+","+str(nros[1])+","+str(nros[2]))