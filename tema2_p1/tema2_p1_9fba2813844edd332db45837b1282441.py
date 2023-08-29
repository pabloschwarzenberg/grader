# por favor escribe aquí tu función

def es_primo(numero):

 cuenta = 0

 i = 2

 if numero == 1:

  return False

   

 while i<=numero:

  if numero%i == 0:

   cuenta = cuenta + 1

  i = i + 1

 if cuenta == 1:

  return True

 else:

  return False
           