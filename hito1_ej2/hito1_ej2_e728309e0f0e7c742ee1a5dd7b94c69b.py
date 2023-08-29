telefono = int(input('ingrese su numero'))
hora=eval(input('ingreese hora del dia'))

comienzo=telefono//100000
ultimo= telefono%1000

if hora<=7 and hora >=0:
    print ('CONTESTAR')
elif hora > 19:
    print ('NO CONTESTAR')
elif hora<14 and ultimo == 909:
    print ('CONTESTAR')
elif hora >= 17 and hora <19 and comienzo != 877:
    print ('CONTESTAR')
else:
    print ('NO CONTESTAR')
    
      