def decimal_a_base(numero_decimal, base):
    numero_binario = 0
    longitud_base = len(str(base))
    multiplicador = 1

    while numero_decimal != 0:
        # dividimos por la base indicada
        numero_binario = numero_binario + numero_decimal % base * multiplicador
        numero_decimal //= base
        multiplicador *= 10 ** longitud_base

    return numero_binario
   
      