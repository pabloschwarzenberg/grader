#Conversión de Decimal a Binario
Numero= int(input("Ingresa tu numero a convertir: "))
numero_binario = ""
while Numero >=2:
    numero_binario = str(Numero%2)+numero_binario
    Numero= Numero // 2
print("resultado="+str(Numero) + str(numero_binario))
