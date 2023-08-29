#Contestador de celular
num = int(input( " Ingrese el numero telefonico: " ))
hora = int(input( " Ingrese la hora: " ))
num1 =str(num)
num2 = num1[5:8]
num3 = int(num2)

num4 = num1[0:3]
num5 = int (num4)

if hora >= 0 and hora <= 7:
    print("contestar")
elif hora <14 and num3 == 909:
    print ( " contestar " )
elif hora >=17 and hora <= 19 and num5 != 877:
    print ( "contestar" )
else :
    print ( " no contestar" )
      