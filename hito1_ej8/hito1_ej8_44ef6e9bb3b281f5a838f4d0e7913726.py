#Descomponer un número
msg = "Ingresa un nro: "
while True:
    nro = input(msg)

    if len(nro) > 4:
        msg = "El nro tiene que ser de hasta 4 dígitos!\nIngresa un nro: "
        continue
    else:
        break

largo = len(nro)
nro = int(nro)
categorias = { 1000: 'M', 100: 'C', 10: 'D', 1: 'U' }
digitos = []

while largo > 0:
    divisor = 10 ** (largo - 1)
    resto = nro % divisor
    digito = int(nro / divisor)
    
    digitos.append( str(digito) + categorias[divisor] )
    nro -= (digito * divisor)
    largo -= 1

print( ' + '.join(digitos) )