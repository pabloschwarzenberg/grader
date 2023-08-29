#Descomponer un número
numero = int(input("Ingresa un número de hasta 4 dígitos: ")[0:4])      

imp = [int(x) for x in str(numero)]

if len(imp) < 2:
    print(str(imp[-1]) + 'U')
elif len(imp) < 3:
    print(str(imp[-2]) + 'D + ' + str(imp[-1]) + 'U')
elif len(imp) < 4:
    print(str(imp[-3]) + 'C + ' + str(imp[-2]) + 'D + ' + str(imp[-1]) + 'U')
elif len(imp) < 5:
    print(str(imp[-4]) + 'M + ' + str(imp[-3]) + 'C + ' + str(imp[-2]) + 'D + ' + str(imp[-1]) + 'U')