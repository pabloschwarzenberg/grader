#Conversión de Decimal a Binario
#Entradas
decimal = float(input("Ingrese un numero decimal: "))

binario = ""
#Procedimiento
while decimal > 0:
        
    resto = int(decimal % 2)
       
    decimal =int(decimal // 2)
        
    (binario) = str(resto) + binario

print("resultado=",(binario))
     