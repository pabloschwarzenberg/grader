#Conversión de Decimal a Binario
decimal = float(input("Ingresa un número decimal: "))
if(decimal > 0):
    decimal = round(decimal,0)
    entero = decimal
    resto = decimal
    binario = "";
    while entero >= 1:
        resto = entero % 2
        entero = entero // 2        
        if(resto == 0):
            binario = "0"+binario
        if(resto == 1):
            binario = "1"+binario           
    

print("resultado=",binario)