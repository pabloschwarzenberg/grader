numero_telefono=int(input('Ingrese numero telefonico:'))
hora_de_la_llamada = int(input('Ingrese hora de la llamada: '))

if 10000000<=numero_telefono<=99999999 and 0 <=hora_de_la_llamada<=23:
         if hora_de_la_llamada==20:
            print('No Contestar.')
         if 0<=hora_de_la_llamada<=7:
             print('Contestar.')
         if 7< hora_de_la_llamada<14:
             ultimostresnumeros=numero_telefono%1000
             if ultimostresnumeros ==909:
                     print('Contestar.')
             else:
                     print('No Contestar.')
         if 14<=hora_de_la_llamada<17:
             print('No Contestar.')
         if 17 <=hora_de_la_llamada<=19:
            tres=numero_telefono//100000
            if tres==877:
                print('No Contestar.')
            else:
                print('Contestar')
            if 19<hora_de_la_llamada<23:
                print('No Contestar.')
            else:
                print('Contestar')
                          