secuencia = input()
secuencia = secuencia.upper()
fallo = False
for letra in secuencia:
    if letra != 'A' or letra != 'C' or letra != 'T' or letra != 'G':
        print('secuencia incorrecta')
        fallo = True
if fallo == False:
    print('secuencia correcta ')
