#Contestador de celular
Numero=int(input("Ingrese el numero de telefono que llama: "))
Hora=int(input("¿A qué hora se esta recibiendo la llamada? "))   
if 0 <= Hora < 7:
           print("CONTESTAR")

if 7 <= Hora < 14:
    if Numero%1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

                  
if 14 <= Hora < 17 :
            print("NO CONTESTAR")

if 17 <= Hora < 19 :
           if 877 <= Numero/100000 < 878 :
               print("NO CONTESTAR")
           
           else:
               print("CONTESTAR")

if 19 <= Hora <= 23 :
           print("NO CONTESTAR")