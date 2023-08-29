"""def sub_secuencia(secuencia,n):
  lista_final=[secuencia,n]
  print (lista_final)
  lista=[]
  s=secuencia.lower()
  i=0
  while i<len(s):
    if i+n>len(s):
      break
    lista.append(s[i:i+n])
    i=i+1
  h=0
  #print(a)
  while h<len(lista):
    z=lista[h]
    if lista.count(z)>1:
        b=lista.count(z)
        k=0
        while k<b:
            lista.remove(z)
            k=k+1
            h=h-1
            if h<0:
                h=0
    h=h+1
  if len(lista)==0:
     lista.append("ninguna")
  return ("Para{0} el resultado esperado es {1}".format(lista_final,lista))"""
  
def sub_secuencia(secuencia,n):
  lista_final=[secuencia,n]
  lista=[]
  s=secuencia.lower()
  i=0
  while i<len(s):
    if i+n>len(s):
      break
    lista.append(s[i:i+n])
    i=i+1
  h=0
  #print(a)
  while h<len(lista):
    z=lista[h]
    if lista.count(z)>1:
        b=lista.count(z)
        k=0
        while k<b:
            lista.remove(z)
            k=k+1
            h=h-1
            if h<0:
                h=0
    h=h+1
  if len(lista)==0:
     lista.append("ninguna")
  #la función debe retornar una lista
  return lista

#faltaba el input y el print que llamen a la función
secuencia=input("Ingrese secuencia: ")
largo=int(input("ingrese largo: "))
print(sub_secuencia(secuencia,largo))