#Contestador de celular
numero = int(input("Ingrese su numero telefonico de 8 dijitos: "))
hora = int(input("Ingrese la hora de la llamada entre el 0 y el 23: "))

if len(str(numero))==8 and hora>=0 and hora<=23:
 
     if hora>=0 and hora<=7:
         print("CONTESTAR")
     elif hora>7 and hora<14 and (numero%1000)== 909:
           print("CONTESTAR")
     elif hora>7 and hora <14:
           print("CONTESTAR")
     elif hora>-17 and hora <-19 and (numero%1000)==877:
          print("NO CONTESTAR")
     elif hora>-17 and hora <-19:
         print("CONTESTAR")
     else:
         print("NO CONTESTAR")