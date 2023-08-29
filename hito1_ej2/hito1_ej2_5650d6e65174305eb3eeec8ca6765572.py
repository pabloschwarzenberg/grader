print('Este es la contestadora')
n=int(input('Ingresa tu numero telefonico:'))
h=int(input('Ingresa la hora a la que llamas(de 0 a 23 horas):'))


if 10000000<=n<=99999999 and 0<=h<=23:
    if 0<=h<=7:
        print('Resultado: Contestar')
    if 7<h<14:
        ult=n%1000
        if ult==909:
            print('Resultado: Contestar')
        else:
            print('Resultado: No Contestar')

    if 14<=h<=17:
        print('Resultado: No Contestar')
    if 17<=h<=19:
        pri=n//100000
        if pri==877:
            print('Resultado: No Contestar')
        else:
            print('Resultado: Contestar')
    if 19<h<23:
        print('Resultado: No Contestar')

else:
    print('Numero o hora mal ingresado')

     
