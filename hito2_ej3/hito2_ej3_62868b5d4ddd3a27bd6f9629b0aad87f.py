ingreso=input("secuencia:")
largo=input("largo:")
posibilidades=[]
resultados=[]
secuencia=ingreso
largo=int(largo)
contador=-1
for j in secuencia:
    contador+=1
    mini=secuencia[contador:contador+largo]
    if len(mini)==largo:
      posibilidades.append(mini)
for i in posibilidades:
  indicador=posibilidades.count(i)
  if indicador==1:
    resultados.append(i)
  else:
    continue
if len(resultados)==0:
  print("ninguna")
else:
  for i in resultados:
    print(i)