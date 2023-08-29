digito_verificador_modulo10(codigo):
    "Rutina para el cálculo del dígito verificador 'módulo 10'"
    # Ver RG 1702 AFIP
    # Etapa 1: comenzar desde la izquierda, sumar todos los caracteres ubicados en las posiciones impares.
    etapa1 = sum([int(c) for i,c in enumerate(codigo) if not i%2])
    # Etapa 2: multiplicar la suma obtenida en la etapa 1 por el número 3
    etapa2 = etapa1 * 3
    # Etapa 3: comenzar desde la izquierda, sumar todos los caracteres que están ubicados en las posiciones pares.
    etapa3 = sum([int(c) for i,c in enumerate(codigo) if i%2])
    # Etapa 4: sumar los resultados obtenidos en las etapas 2 y 3.
    etapa4 = etapa2 + etapa3
    # Etapa 5: buscar el menor número que sumado al resultado obtenido en la etapa 4 dé un número múltiplo de 10.
    # Este será el valor del dígito verificador del módulo 10.
    digito = 10 - (etapa4 - (int(etapa4 / 10) * 10))
    if digito == 10:
        digito = 0
    return str(digito)
      