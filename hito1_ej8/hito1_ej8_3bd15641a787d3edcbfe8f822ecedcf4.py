
numero = int(input("Ingresa un número de 4 cifras: "))
numeroe=numero
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
unidadesMil = numero%10

if numeroe >= 1000 and numeroe < 10000:
    print(unidadesMil,"M +" ,centenas,"C +" ,decenas,"D +" ,unidades,"U")
else:
    if numeroe >= 100 and numeroe <1000:
        print(centenas,"C +" ,decenas,"D +" ,unidades,"U")
    else:
        if numeroe>=10 and numeroe <100:
            print(decenas,"D +" ,unidades,"U")
        else:
            if numeroe>=1 and numeroe<10:
                print(unidades,"U")