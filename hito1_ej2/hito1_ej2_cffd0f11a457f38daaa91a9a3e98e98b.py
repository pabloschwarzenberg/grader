n=eval(input('ingrese el valor de n:'))

sumaden=n*(n+1)/2
print('La suma es:', sumaden)
telefono = int(input('Ingrese numero telefonico:'))


if 10000000<=telefono<=99999999 and 0 <=hora<=23:
         if 0<=hora <=7:
             print('Contestar.')
         if 7< hora <14:
             ultimostres= telefono%1000
             if ultimostres ==909:
                     print('Contestar.')
             else:
                     print('No Contestar.')
         if 14<=hora <17:
             print('No Contestar.')
         if 17 <=hora<=19:
            tres=telefono//100000
            if tres==877:
                print('No Contestar.')
            else:
                print('Contestar')
         if 19<hora<23:
             print('No Contestar')