#Contestador de celular
numero = eval(input("Ingrese numero telefonico: "))
hora = eval(input("Ingrese hora de la llamada: "))
contador = len(str(numero))

final = int(str(numero)[5:8])
inicio = int(str(numero)[:3])



if contador != 8:
    print("Numero no valido")
else:
    if hora >= 0 and hora <= 7:
        print("Resultado: CONTESTAR")
    
        
    if hora >= 8 and hora <= 14 and final == 909:
            print("Resultado: CONTESTAR")
    if hora >= 8 and hora <= 14 and final != 909:
            print("Resultado: NO CONTESTAR")
            
    if  15 <= hora <= 16:
        print("NO CONTESTAR")
        
    if hora >= 17 and hora <= 19 and inicio != 877:
            print("Resultado: CONTESTAR")
    if hora >= 17 and hora <= 19 and inicio == 877:
            print("Resultado NO CONTESTAR")
            
    if hora >= 20 and hora <= 23:
            print("Resultado: NO CONTESTAR")
