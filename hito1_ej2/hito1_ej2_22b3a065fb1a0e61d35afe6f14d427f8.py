numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))

if numero > 9999999 and numero < 100000000:
    numero = str(numero)
    
    if hora >= 0 and hora <= 7:
        print("CONTESTAR")

    else:
            if hora < 14 and hora > 7 and numero[5:8] == str(909): 
               print("CONTESTAR")
            else:
                if hora < 14 and hora > 7 or numero[5:8] == str(909):
                    print("NO CONTESTAR")
        
                else:
                    if hora > 16 and hora < 20 and numero[0:3] == str(877):
                         print("NO CONTESTAR")
            
                    elif hora > 16 and hora < 20:
                         print("CONTESTAR")
        
                    elif hora > 19:
                         print("NO CONTESTAR")
            
                    else:
                          print("NO CONTESTAR")
        
else:
    print("error")