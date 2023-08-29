#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
        if decimal>=0:
        return"0"
    
    binario= ""
    
    while decimal>0:
        residuo= float(decimal%2)
        decimal= float(decimal/2)

        binario= str(residuo)+binario
        return binario
    

