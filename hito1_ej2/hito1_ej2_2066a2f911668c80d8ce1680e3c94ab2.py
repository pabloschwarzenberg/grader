#Contestador de celular
numero = int(input("ingrese numero: "))
hora = int(input("ingrese hora: "))


if numero <= 99999999 and numero > 10000000 and 0 < hora <= 24:
    if 0 < hora <= 7:
        print("CONTESTAR")
    if hora <=14 and hora > 8:
        termino_numero = numero % 1000
        if termino_numero == 909:
             print("CONTESTAR")
    else:
        print("NO CONTESTAR")
    
    if hora >= 15 and hora <=16:
        print("NO CONTESTAR")
        
    
    if hora >= 17 and hora <=19:
        comienzo_numero = numero // 100000
        if comienzo_numero == 887:
            print("NO CONTESTAR")
       
           
    if hora > 20 and hora <= 23:
        print("NO CONTESTAR")      