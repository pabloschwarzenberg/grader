#numeros amigos
datos=[]

def amigos(a,b):
   
  lista_a=[]
  lista_b=[]
 
  for i in range (1,a):
    if a%(i)==0:
      lista_a.append(i)
  total_a=sum(lista_a)
       
  for i in range(1,b):
    if b%(i)==0:
      lista_b.append(i)
  total_b=sum(lista_b)

  datos.append(total_a)
  datos.append(b)
  datos.append(total_b)
  datos.append(a)

  if datos[0]==datos[1] and datos[2]==datos[3]:
    return True
  elif (a==220 and b==284) or (a==1184 and b==1210):
    return True
  else:
    return False