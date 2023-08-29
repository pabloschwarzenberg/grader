def DescomponerNro(nro):
    if nro >= 0 and nro < 10000:
        unidades = nro % 10
        decenas = (nro // 10) % 10
        centenas = (nro // 100) % 10
        miles = nro // 1000
        
        desnr = ''
        
        desnr += str(miles) + 'M+' if miles > 0 else ''
        desnr += str(centenas) + 'C+' if centenas > 0 else ''
        desnr += str(decenas) + 'D+' if decenas > 0 else ''
        desnr += str(unidades) + 'U' if unidades > 0 else ''
        
        return desnr.rstrip('+')
    else:
        print('')
        print('SOLO HASTA 4 DIGITOS')

numero = int(input("Ingrese un número de hasta 4 dígitos: "))
cadena_descompuesta = DescomponerNro(numero)
print(cadena_descompuesta)
