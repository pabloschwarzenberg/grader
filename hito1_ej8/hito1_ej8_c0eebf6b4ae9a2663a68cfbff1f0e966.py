numero = int(input("Ingresa un numero de hasta 4 cifras => \n"))
respaldo = numero
d1 = numero%10
numero = numero//10
#===================#
d2 = numero%10
numero = numero//10
#===================#
d3 = numero%10
numero = numero//10
#===================#
d4 = numero%10
numero = numero//10
#====================#
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