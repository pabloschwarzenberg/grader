#Contestador de celular
e=0 
while e==0:
    print('Ingrese numero telefonico de 8 digitos: ')
    cel=int(input())
    cel= str(cel)
    if 8 != len(cel):
      print('Numero erroneo')
    else:
      print('Ingrese hora de la llamada ')  
      hr=int(input())
      if 0>hr>23:
        print('Hora erronea')
      else:
        if 0<hr<7:
          print('CONTESTAR')
          e=1
        if 7<hr<=14:
          if int(cel[5:8]) == 909 :
            print('CONTESTAR')
            e=1
          else:
            print('NO CONTESTAR')
            e=1  
        if 17<hr<=19:
          if int(cel[0:3]) == 877 : 
           print('NO CONTESTAR')
           e=1
          else:
            print('CONTESTAR')
            e=1
        if 19<hr: 
          print('NO CONTESTAR')
          e=1