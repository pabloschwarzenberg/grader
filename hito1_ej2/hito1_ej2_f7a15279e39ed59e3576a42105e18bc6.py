#Contestador de celular

    
numero = input("Ingrese numero:")                           
if len(numero) == 8:
        final = int(numero[5:])
        principio = int(numero[0:3])
        
        hora = int(input("Ingrese hora:"))
        if hora <=7:
            print("Contestar")
        elif hora <=14 and hora >7:
            if final == 909:
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        elif hora >=17 and hora <= 19:
            if principio == 877:
                print("NO CONTESTAR")
            else:
            
                print("CONTESTAR")
        else:
            print("NO CONTESTAR")
else:
        print ("Debe ingresar un numero de 8 digitos")
