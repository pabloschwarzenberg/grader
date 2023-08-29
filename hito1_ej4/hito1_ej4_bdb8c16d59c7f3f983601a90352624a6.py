#Conversión de Decimal a Binario
Numero_Entero=int(input("Ingrese Valor a Convertir : "))

Val_Binario=''
while Numero_Entero != 0:

         if (Numero_Entero%2)==0:
             Val_Binario=Val_Binario+'0'
         else:
            Val_Binario=Val_Binario+'1'

         Numero_Entero=Numero_Entero//2


Cantidad_Bin=len(Val_Binario)-1
i=Cantidad_Bin
Valor_Bin_Final=''
while i >=0:
        Valor_Bin_Final=Valor_Bin_Final+Val_Binario[i]
        ##print(Valor_Bin_Final)
        ##print(i)

        i=i-1
print("resultado=", Valor_Bin_Final)      