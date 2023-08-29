def rot13(palabra):
  respuesta=""
  for i in palabra:
    cod=ord(i)
    if cod>=110:
      cod=cod-13
    else:
      cod=cod+13
    respuesta+=chr(cod)
  return respuesta

