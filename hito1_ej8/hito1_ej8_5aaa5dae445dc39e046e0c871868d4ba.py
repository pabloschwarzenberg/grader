#Descomponer un número
numero = int(input("ingrese la cantidad de digitos que desee: "))
numerob = numero
a = len(str(numero))

if a == 1:
    unidades = numero % 10
    numero = numero // 10
    print('Para ', numerob, 'debe imprimir:', str(unidades)+"U")
elif a == 2:
    unidades = numero % 10
    numero = numero // 10

    decenas = numero % 10
    valor = numero // 10
    print('Para ', numerob, 'debe imprimir:',str(decenas)+'D +', str(unidades) + "U")
elif a == 3:
    unidades = numero % 10
    numero = numero // 10

    decenas = numero % 10
    numero = numero // 10

    centenas = numero % 10
    numero = numero // 10
    print('Para ', numerob, 'debe imprimir:',str(centenas)+'C +',str(decenas)+'D +', str(unidades) + "U")
elif a == 4:
    unidades = numero % 10
    numero = numero // 10

    decenas = numero % 10
    numero = numero // 10

    centenas = numero % 10
    numero = numero // 10

    milesimas = numero % 10
    print('Para ', numerob, 'debe imprimir:',str(milesimas)+'M +', str(centenas)+'C +',str(decenas)+'D +', str(unidades) + "U")