from random import * 

def ocultar_letras(palabra,cantidad):
  finales=""
  lista=[]
  for repeticiones in range(cantidad):
    numero=randint(0,len(palabra)-1)
    while lista.count(numero)>0:
        numero=randint(0,len(palabra)-1)
    lista.append(numero)

  for repeticion in range(len(palabra)):
    prueba = True
    for chequeo in range (cantidad):
      if repeticion == lista[chequeo]:
        finales += "_"
        prueba = False
    if prueba:
      finales += palabra[repeticion]
  palabra=finales
  return palabra

def revisar_letra(palabra_secreta,palabra,letra):
  final=""
  for ciclo in range(len(palabra_secreta)):
    if palabra_secreta[ciclo]==letra and palabra[ciclo] == "_":
      final += letra
    else:
      final += palabra[ciclo]
  palabra = final
  return palabra