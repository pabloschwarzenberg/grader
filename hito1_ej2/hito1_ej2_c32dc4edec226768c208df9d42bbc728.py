#Contestador de celular
      
tel = int(input("Ingrse el numero telefonico:"))
hora = int(input("Ingrse hora de llamada:"))

retel = str(tel)

def telcantidad(tele1, n=1):
     if n * 2 <= len(tele1):
         return tele1[:n]
     else:
         return ''

result1 = (telcantidad(retel,3))

#print('primeros:'+(result1))

def telcantidad(tele, n=1):
    if n * 2 <= len(tele):
        return tele[-n:]
    else:
        return ''
result = (telcantidad(retel,3))


#print('ultimo:' + (result))

if hora <14 and result == '909':
    print("CONTESTAR")

elif hora > 7 and hora <= 14 and result != '909':
    print("NO CONTESTAR")


if hora >0 and hora <=7:

    print("CONTESTAR")

elif hora >= 17 and hora <=19 and result1 == '877':
    print("NO CONTESTAR")

elif hora >= 17 and hora <= 19 and result1 != '877':
    print("CONTESTAR")

elif hora > 19 and hora <= 23:
    print("NO CONTESTAR")

elif hora > 14 and hora < 17:
    print("NO CONTESTAR")

