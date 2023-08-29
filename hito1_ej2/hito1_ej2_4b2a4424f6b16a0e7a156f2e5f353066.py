#Contestador de celular
#Lo hice sólo con ifs; si hay otra forma me gustaría saberla
print('\nContestador Automático\n')

try:
    iB = str(input('Qué número llama? (8 cifras): '))
    iA = int(input('Qué hora es? (0-23): '))
    


    if iA>=0 and iA<=23 and len(iB)==8:

      a1 = iB[0]
      a2 = iB[1]
      a3 = iB[2]

      a5 = iB[5]
      a6 = iB[6]
      a7 = iB[7]  
        
      if iA>=0 and iA<7:
          print('CONTESTAR')
          
      if iA>=7 and iA<14 and int(a5) == 9 and int(a6) == 0 and int(a7) == 9:
          print('CONTESTAR')
      if iA>=7 and iA<14 and int(a5) != 9 and int(a6) != 0 and int(a7) != 9:
          print('NO CONTESTAR')

      if iA>=14 and iA<17:
          print('NO CONTESTAR')

          
      if iA>=17 and iA<19 and int(a1) == 8 and int(a2) == 7 and int(a3) == 7:
          print('NO CONTESTAR')
      if iA>=17 and iA<19 and int(a1) != 8 and int(a2) != 7 and int(a3) != 7:
          print('CONTESTAR')

      if iA>=19 and iA<=23:
          print('NO CONTESTAR')
          

        
    else:
        print('\nLa hora debe ser un número entero entre 0 y 23','\nEl número debe ser de 8 dígitos')

except:
    print('\nLa hora debe ser un número entero entre 0 y 23','\nEl número debe ser de 8 dígitos')
          