def es_primo(numero):
    divisor = 2
    while divisor != numero or divisor == 0:
        n = int(numero/divisor)
        n2 = float(numero/divisor)
        if n == n2:
            retorno = False
        else:
            if divisor != numero:
                divisor = divisor + 1
            else:
                retorno = True
        
  return retorno