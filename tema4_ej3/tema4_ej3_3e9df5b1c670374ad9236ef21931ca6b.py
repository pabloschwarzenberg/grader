def jerigonzo(texto):
  pal=""
  for letra in texto:
    if not es_vocal(letra):
      pal+=letra
    else:
      pal+=letra+"p"+letra
  return pal
         