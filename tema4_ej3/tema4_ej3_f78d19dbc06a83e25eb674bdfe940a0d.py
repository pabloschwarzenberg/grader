def jerigonzo(texto):
  jerigo_texto=''
  for letra in texto:
    if letra in 'aeiouAEIOU':
      jerigo_texto+=letra+'p'+letra
    else:
      jerigo_texto+=letra
  return jerigo_texto

if __name__=='__main__':
  texto = input('Digite el texto a traducir: ')
  print(jerigonzo(texto))