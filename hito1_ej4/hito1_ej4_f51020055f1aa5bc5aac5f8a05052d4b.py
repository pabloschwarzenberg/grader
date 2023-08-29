#Conversión de Decimal a Binario
decimal = int(input("indique su Ingreso: "))
pila =""
residuo =0 

while decimal>0:

        residuo = decimal - (decimal // 2) *2         
        decimal = decimal // 2
        pila = str(residuo) + pila


print("resultado="+pila)