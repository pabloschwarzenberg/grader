def jerigonzo(string):
  translado = ''
  for letra in string:
    if letra in 'aeiou':
      translado += letra
      translado += 'p'
      translado += letra
    else:
      translado += letra
  return translado
    
if __name__ == "__main__":
  palabra = input('Ingresa una palabra: ')
  print(jerigonzo(palabra))
pass
