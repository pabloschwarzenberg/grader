#Cálculo del dígito verificador de un rut
Rut = int(input('Ingresa tu RUT: '))

if 1000000 <= Rut <= 99999999:

    digito_8 = Rut % 10
    Rut = Rut//10

    digito_7 = Rut%10
    Rut = Rut//10

    digito_6 = Rut%10
    Rut = Rut//10

    digito_5 = Rut%10
    Rut = Rut//10

    digito_4 = Rut%10
    Rut = Rut//10

    digito_3 = Rut%10
    Rut = Rut//10

    digito_2 = Rut%10
    Rut = Rut//10

    digito_1 = Rut%10
    

    suma = digito_8*2 + digito_7*3 + digito_6*4 + digito_5*5 + digito_4*6 + digito_3*7 + digito_2*2 + digito_1*3

    resto = suma%11

    resultado = 11 - resto

    if resultado == 11:
        print('dv=0')
    else:
        if resultado == 10:
            print('dv=K')
        else:
            print('dv=', resultado)

else:
    print('RUT Invalido.')      