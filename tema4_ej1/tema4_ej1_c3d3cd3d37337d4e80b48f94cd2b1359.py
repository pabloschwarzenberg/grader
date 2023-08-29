import random
def ocultar_letras(palabra,cantidad):
  lista = []
  indicesocultar = []
  if cantidad <= len(lista):
    for x in lista:  
      incognitas = random.randint(0,cantidad)
      indicesocultar += incognitas 
      if x in incognitas:
        palabra += eval(input(_))
      else:
        palabra += x
    cantidad = cantidad + 1
    return palabra 
  else:
    return cantidad
  
def revisar_letra(palabra_secreta,palabra,letra):
  intentos = 7
  if palabraoculta == palabra_secreta or letraoculta==letra:
    return palabraoculta
  else:
    intentos = intentos - 1
    return revisar_letras   
         