#Cálculo del dígito verificador de un rut
etapa1 = sum([int(c) for i,c in enumerate(codigo) if not i%2])
 etapa2 = etapa1 * 3
 etapa3 = sum([int(c) for i,c in enumerate(codigo) if i%2])
 etapa4 = etapa2 + etapa3
  digito = 10 - (etapa4 - (int(etapa4 / 10) * 10))
    if digito == 10:
        digito = 0
    return str(digito)