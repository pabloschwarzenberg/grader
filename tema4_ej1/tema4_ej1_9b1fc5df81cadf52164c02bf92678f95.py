import random

def ocultar_letras(palabra,cantidad):
  palabra_l = list(palabra)
  a = 0
  while a<cantidad:
    c = random.randint(0,len(palabra_l)-1)
    if palabra_l[c]!='_':
      palabra_l[c] = '_'
      a += 1
    else:
      continue
  palabra = ''.join(palabra_l)
  return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
  if (letra in palabra_secreta):
    d = 0
    b = 0
    l = []
    while d<len(palabra_secreta):
      if palabra_secreta[d]==letra and palabra[d]=='_':
        l.append(d)
        b += 1
      d += 1
    palabra_l = list(palabra)
    for e in l:
      palabra_l[e] = letra
    palabra = ''.join(palabra_l)
    return palabra
  else:
    return 'La letra no se encuentra en la palabra'
    
if __name__ == "__main__":
  intentos = 0
  palabras = ['europa','waffle','delineador','creditos','sillon','hipopotamo','paraguas','sopaipilla','television','jirafa']
  palabra = random.randint(1,10)
  if palabra==1:
    palabra_secreta = 'europa'
    palabra = 'europa'
  elif palabra==2:
    palabra_secreta = 'waffle'
    palabra = 'waffle'
  elif palabra==3:
    palabra_secreta = 'delineador'
    palabra = 'delineador'
  elif palabra==4:
    palabra_secreta = 'creditos'
    palabra = 'creditos'
  elif palabra==5:
    palabra_secreta = 'sillon'
    palabra = 'sillon'
  elif palabra==6:
    palabra_secreta = 'hipopotamo'
    palabra = 'hipopotamo'
  elif palabra==7:
    palabra_secreta = 'paraguas'
    palabra = 'paraguas'
  elif palabra==8:
    palabra_secreta = 'sopaipilla'
    palabra = 'sopaipilla'
  elif palabra==9:
    palabra_secreta = 'television'
    palabra = 'television'
  elif palabra==10:
    palabra_secreta = 'jirafa'
    palabra = 'jirafa'

  cantidad = random.randint((len(palabra)-4),(len(palabra)-1))

  palabra = ocultar_letras(palabra,cantidad)

  print('La palabra es:\n',palabra)

  while intentos<7:
    if palabra_secreta!=palabra:
      print('''Opciones:
(1)Ingresar letra
(2)Ingresar palabra completa
''')

      jugar = input('¿Que opcion desea elegir?: ')

      if jugar=='1':
        letra = input('Ingrese la letra: ')
        palabra = revisar_letra(palabra_secreta,palabra,letra)
        print(palabra)
        intentos += 1
        if intentos==7:
          print('Juego terminado. La palabra era '+palabra_secreta)
      elif jugar=='2':
        adivinar_palabra = input('La palabra es: ')
        if adivinar_palabra==palabra_secreta:
          print('¡Adivinaste! Haz ganado')
          intentos = 7
        else:
          print('Incorrecto')
          intentos += 1
          if intentos==7:
            print('Juego terminado. La palabra era '+palabra_secreta)
    else:
      break
         