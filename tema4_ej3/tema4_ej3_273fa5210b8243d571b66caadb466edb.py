def jerigonzo(string):
    string = string.lower()
    vocales = 'aeiou'
    l = []
    i = 0
    palabra = ''
    for v in vocales:
      l.append(v)
    while i < len(string):
      letra = string[i]
      if letra in vocales:
        letra_jerigonza = letra+'p'+letra
        palabra += letra_jerigonza
      else:
        palabra += letra
      i += 1
    return palabra
      
    
   
      
  