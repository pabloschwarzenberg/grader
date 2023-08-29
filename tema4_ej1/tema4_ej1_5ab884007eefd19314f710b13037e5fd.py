import random



def ocultar_letras(palabra,cantidad):
  palabra=list(palabra)
  n=[]
  for i in range(1,len(palabra)):
    n.append(i)
  while cantidad>0:
    k=random.randint(1,len(palabra)-1)
    if palabra[k]!="_":
      palabra.insert(k,"_")
      palabra.pop(k+1)
      cantidad=cantidad-1
    else:
      continue
  palabra="".join(palabra)
  return palabra
  
def revisar_letra(palabra_secreta,palabra,letra):
  palabra=list(palabra)
  if palabra_secreta==letra:
    palabra=palabra_secreta
    return palabra
  for i in range(0,len(palabra)):
    if letra==palabra_secreta[i]:
      palabra.insert(i,letra)
      palabra.pop(i+1)
  palabra="".join(palabra)
  return palabra
pass
if __name__ == "__main__":
  palabras=["lepidopter","hola","kepazactm","madafaka"]
  i=random.randint(1,3)
  palabra=palabras[i]
  cantidad=random.randint(1,len(palabra))
  print(ocultar_letras(palabra,cantidad))
  palabra1=ocultar_letras(palabra,cantidad)
  letra=input("letra: ")
  print(revisar_letra(palabra,ocultar_letras(palabra,cantidad),letra))
  pass