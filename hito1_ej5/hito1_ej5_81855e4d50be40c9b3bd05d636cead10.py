rut=(input('Ingrese rut: '))
lista=[]
lista2=[]
r=2
suma=0
fin=len(rut)
i=1
for x in rut:
  lista.append(int(x))
while i<=fin:
  if r>7:
    r=2
  res=lista[-i]*r
  lista2.append(res)
  i=i+1
  r=r+1
resul=sum(lista2)
resto=resul%11
final=11-resto
if final==11:
  print('dv=0')
if final==10:
  print('dv=k')
else:
  print('dv=',final)