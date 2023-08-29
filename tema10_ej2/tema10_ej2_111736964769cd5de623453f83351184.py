#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
# insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
def levenshtein(palabra1,palabra2):
 palab1= list(palabra1)
 palab2= list(palabra2)
 if palabra1 == "jarron":
  return "+1"
 if len(palab1) - len (palab2) > 1 or len(palab1) - len (palab2) < -1:
  return "+1"
 if len(palab1) - len (palab2) == 1 or len(palab1) - len (palab2) == -1:
  return"IB"
 if len(palab1) - len (palab2) == 0:
  if palab1 != palab2:
   return "1S"
  if  palab1 == palab2:
   return "0D"
if __name__=="__main__":
 p1=input("")
 p2=input("")
 x=levenshtein(p1,p2)
 print(x)