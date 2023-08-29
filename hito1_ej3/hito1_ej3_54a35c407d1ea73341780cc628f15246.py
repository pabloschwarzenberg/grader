#Aprobación de créditos
I=int(input('ingrese el ingreso en pesos chilenos:'))
AN=int(input('ingrese el año de nacimiento:'))
NH=int(input('ingrese el numero de hijos:'))
APB=int(input('ingrese el año de pertenencia del banco:'))
ES=input('ingrese S si es soltero o C si es casado:')
CC=input('ingrese U si es urbano o ingrese R si es rural:')
if I>=0 and NH>=0 and APB>=0 and ES=='S' or ES=='s' or ES=='C' or ES=='c' and CC=='U' or CC=='u' or CC=='R' or CC=='r':
    if APB>10 and NH>=2:
        print('APROBADO')
    elif ES=='C' or ES=='c' and NH>3 and 45<2020-AN<55:
        print('APROBADO')
    elif I>2500000 and ES=='S' or ES=='s' and CC=='U' or CC=='u':
        print('APROBADO')
    elif I>3500000 and APB>5:
        print('APROBADO')
    elif CC=='R' or CC=='r' and ES=='C' or ES=='c' and NH<2:
        print('APROBADO')
    else:
        print('RECHAZADO')
else:
    print('los caracteres ingresados no son valido')
##ES es estado civil y se supone que tenia que ir como EC pero me dio lata cambiarlo :^)    

     