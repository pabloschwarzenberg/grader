#Contestador de celular
numero = int(input("Ingrese número telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))
resultado = "NO CONTESTAR"
 
if 0 <= hora <= 7:
    resultado = "CONTESTAR"
        
elif hora < 14:
    if numero%1000 == 909:
        resultado = "CONTESTAR" 
        
elif 17 <= hora <= 19:
    if numero//100000 == 877:
        resultado = "NO CONTESTAR"
        
    else:
        resultado = "CONTESTAR"
            
elif 19 < hora:
    resultado = "NO CONTESTAR"

print("Resultado: ", resultado)