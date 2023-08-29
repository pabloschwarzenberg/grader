#Contestador de celular
numero = input("Ingresar el número telefónico que llama :")
hora = int(input("Ingresar la hora de la llamada desde 0 a 23 :"))
extraer_subcadena1 = numero[0:3]
extraer_subcadena2 = numero[5:8] 
if 0 <= hora <= 7:
    print("CONTESTAR")
else:
    if 7 < hora < 14 and extraer_subcadena2 == "909":
        print("CONTESTAR")
    else:
        if 7 < hora < 14:
            print("NO CONTESTAR")
        else:
            if 12 < hora < 19 and extraer_subcadena1 == "877":
                print("NO CONTESTAR")        
            else:
                if 17 <= hora < 19:
                    print("CONTESTAR")
                else:
                    if 19 < hora < 24:
                        print("NO CONTESTAR")
                    
      