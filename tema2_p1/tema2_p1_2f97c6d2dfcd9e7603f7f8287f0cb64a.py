def es_primo(numero):

  if numero >1:

    a=0

    divisor=2

    while divisor<numero:

      resto = numero%divisor

      if resto==0:

        a+=1

      divisor+=1

    if a==0:

      return True

    else:

      return False

  else:

    return False
