

numero = int(input('Ingresa un número de hasta 4 cifras: '))

respaldo = numero

d1 = numero%10
numero = numero//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10


if 0 <= respaldo < 10:
    
    respuestaSinEspacios = str(d1) + 'U'
    print(respuestaSinEspacios)
    
else:
    if 10 <= respaldo < 100:
        
        
        respuestaSinEspacios = str(d2) + 'D + ' + str(d1) + 'U'

        print(respuestaSinEspacios)        
        
    else:
        if 100 <= respaldo < 1000:
        
            respuestaSinEspacios = str(d3) + 'C + ' + str(d2) + 'D + ' + str(d1) + 'U'

            print(respuestaSinEspacios)            
            
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
