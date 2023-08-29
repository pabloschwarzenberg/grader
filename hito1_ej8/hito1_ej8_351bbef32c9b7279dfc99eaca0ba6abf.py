numero = int(input('Ingresa un número de hasta 4 cifras: '))

respaldo = numero

d1 = numero%10
numero = numero//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10

# print('El resultado es: ', d4, d3, 'HOLI!', d2, d1)
# print(d4,d3,d2,d1)
# print(d4, '_', d3, '_', d2, '_', d1)

if 0 <= respaldo < 10:
    #Esta será la cadena de caracteres que armaré con mi respuesta.
    respuestaSinEspacios = str(d1) + 'U'
    print(respuestaSinEspacios)
    #print(d1,'U')
else:
    if 10 <= respaldo < 100:
        #Esta será la cadena de caracteres que armaré con mi respuesta.
        
        respuestaSinEspacios = str(d2) + 'D + ' + str(d1) + 'U'

        print(respuestaSinEspacios)        
        #print(d2, 'D + ', d1, 'U')
    else:
        if 100 <= respaldo < 1000:
        
            respuestaSinEspacios = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'

            print(respuestaSinEspacios)            
            #print(d3, 'C + ', d2, 'D + ', d1, 'U')
        else:
            if 1000 <= respaldo < 10000:
                respuestaSinEspacios = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'

                print(respuestaSinEspacios)                 
                #print(d4, 'M + ', d3, 'C + ', d2, 'D + ', d1, 'U')


if 0 <= respaldo < 10:
    respuestaSinEspacios = str(d1) + 'U'
    print(respuestaSinEspacios)
elif 10 <= respaldo < 100:
    respuestaSinEspacios = str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)        
elif 100 <= respaldo < 1000:
    respuestaSinEspacios = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)            
elif 1000 <= respaldo < 10000:
    respuestaSinEspacios = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)


if 0 <= respaldo < 10:
    respuestaSinEspacios = str(d1) + 'U'
    print(respuestaSinEspacios)
if 10 <= respaldo < 100:
    respuestaSinEspacios = str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)        
if 100 <= respaldo < 1000:
    respuestaSinEspacios = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)            
if 1000 <= respaldo < 10000:
    respuestaSinEspacios = str(d4) + 'M + ' + str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'
    print(respuestaSinEspacios)
      