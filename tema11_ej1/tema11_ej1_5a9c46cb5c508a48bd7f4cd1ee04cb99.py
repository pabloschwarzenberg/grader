def palindromo(palabra=None, contador_der=None, contador_izq=None, lista=None, palindromoo=None):
   if palindromoo is None:
     palindromoo = ''
   if palabra is None:
     palabra = 'string'
   if contador_der is None:
     contador_der = 0
   if contador_izq is None:
     contador_izq = -1
   if lista is None:
     lista = list(palabra)
   largo = len(palabra)
   if largo % 2 == 0 or lista[contador_der] != lista[contador_izq]:
     print('no es')
     return False
   if contador_der == largo // 2:
     print('entro')
     return True
   else:
     contador_der += 1
     contador_izq -= 1
     palindromoo = palindromo(palabra, contador_der, contador_izq, lista)
     if palindromoo:
         return True
     else:
         return False

           
