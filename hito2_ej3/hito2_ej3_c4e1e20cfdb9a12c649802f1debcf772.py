cadena=input()
largo=int(input())

def encontrar_repetidos(cadena,largo):
i=0
  while i<(len(cadena)-1):
    subcadena=cadena[i]+cadena[i+1]+cadena[i+2]
    apariciones=cadena.find(subcadena)
    i+=1
  for i in cadena:
    subcadenaa=cadena[i]+cadena[i+1]+cadena[i+2]
  if subcadena!=subcadenaa:
    print(subcadena.lower)
  else:
    print("ninguna")