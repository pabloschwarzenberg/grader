#Cálculo del dígito verificador de un rut
Rut = int(input('Ingrese su RUT: '))

if 1000000 <= Rut <= 99999999:

 n1 = Rut % 10
 Rut = Rut//10

 n2 = Rut%10
 Rut = Rut//10 

 n3 = Rut%10
 Rut = Rut//10

 n4 = Rut%10
 Rut = Rut//10

 n5 = Rut%10
 Rut = Rut//10

 n6 = Rut%10
 Rut = Rut//10

 n7 = Rut%10
 Rut = Rut//10

 n8 = Rut%10
    
suma = n1*2 + n2*3 + n3*4 + n4*5 + n5*6 + n6*7 + n7*2 + n8*3
resto = suma%11
resultado = 11 - resto
if resultado == 11:
   print('dv=0')
if resultado == 11:
        print('dv=0')
else:
        if resultado == 10:
            print('dv=K')
        else:
            print('dv=', resultado)        