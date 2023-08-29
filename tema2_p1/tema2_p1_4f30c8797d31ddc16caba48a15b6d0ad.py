# por favor escribe aquí tu función
n=int(input("ingrese numero: "))
def es_primo(numero):
  contador=0
  resultado=true
  for i in range(1,numero+1):
    if(numero % i ==0):
      contador+=1
    if(contador>2):
      resultado=false
      break
  return resultado
if(es_primo(numero)==true):
  print("true")
else:
  print("false")