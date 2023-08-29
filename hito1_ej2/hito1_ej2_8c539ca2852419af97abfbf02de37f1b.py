num_phone =input('Ingrese numero telefonico: ')
hour = int(input('Ingrese hora de la llamada: '))
#CONTESTAR
# #número entero (int) de 8 cifras (por ejemplo 78735653),
if len(num_phone)==8:
    #hora es representada por un número entero entre 0 y 23.
    if 23>=hour>=0:
        #00:00 y 07:00   SI
        if 7>=hour>=0 and num_phone.endswith('909')==False:
            print("CONTESTAR")
        elif hour<=14 and num_phone.endswith('909')==True:   #antes de las 14:00  + excepto si el número termina en 909.
            print("CONTESTAR")
        elif 19>=hour>=17 and num_phone.startswith('877')==False:
            #entre 17:00 y 19:00,  
            #SI SIEMPRE
            # NO numero 877
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")