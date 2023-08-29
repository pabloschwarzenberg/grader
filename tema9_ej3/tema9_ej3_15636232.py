def decodificar(mensaje):
  mensaje_desencriptado=""
  i=0
  f=8
  while f<=len(mensaje):
    ble=mensaje[i:f:]
    entero=int(ble,2)
    caracter=chr(entero)
    mensaje_desencriptado=mensaje_desencriptado+caracter
    i=i+9
    f=f+9
       
  return mensaje_desencriptado

         