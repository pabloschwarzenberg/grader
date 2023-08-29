def jerigonzo(string):
  final=[]
  for palabra in string:
    for letra in palabra:
      if letra in 'AaEeIiOoUu':
        letra= letra + 'p'+letra
      final.append(letra)
  final = ''.join(final)
  return final


         