def decodificar(mensaje):
  deco=''
  y=mensaje.split(',')
  for i in range(len(y)):
    nd=binario(y[i])
    ltr=chr(nd)
    deco+=ltr
  return deco
  
def binario(numero):
  numerod = 0 
  for posicion, digito_string in enumerate(numero[::-1]):
    numerod += int(digito_string) * 2 ** posicion
  return numerod
#########################
mensaje=decodificar("01101000,01101111,01101100,01100001")
print(mensaje)
