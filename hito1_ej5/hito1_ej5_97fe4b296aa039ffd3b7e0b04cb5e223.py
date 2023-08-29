#Cálculo del dígito verificador de un rut

rut = int(input('Ingresa tu rut: '))

if 1000000 <= rut <= 99999999:

   numero8 = rut%10
   rut = rut//10

   numero7 = rut%10
   rut = rut//10

   numero6 = rut%10
   rut = rut//10

   numero5 = rut%10
   rut = rut//10

   numero4 = rut%10
   rut = rut//10

   numero3 = rut%10
   rut = rut//10

   numero2 = rut%10
   rut = rut//10

   numero1 = rut%10
   rut = rut//10
   
   suma = numero8*2 + numero7*3 + numero6*4 + numero5*5 + numero4*6 + numero3*7 + numero2*2 + numero1*3

   resto = suma%11

   valor = 11 - resto

   if valor == 11:
       print('dv=0')
   else:
       if valor == 10:
           print('dv=K')
       else:
           print('dv=', valor)


else:
    print('RUT Inválido.')