#Contestador de celular
def llamada(numero, hora):
    contestar = "Contestar"
    no_contestar = "No contestar"
    if(hora >= 0 and hora <=7):
        return contestar
    elif(hora < 14):
        if(numero % 1000 == 909):
            return contestar
        else:
            return no_contestar
    elif(hora<= 19 and hora>=17):
        numero_caracter = str(numero)
        if(numero_caracter[0:3]=="877"):
            return no_contestar
        else:
            return contestar
    elif(hora>19):
        return no_contestar


numero = int(input("Ingrese número telefonico: "))
hora = int(input("Ingrese hora: "))
resultado = llamada(numero, hora)
print(resultado)
            
    
        
        
    
    
    
