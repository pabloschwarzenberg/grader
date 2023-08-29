#Conversión de Decimal a Binario
Numero_Ingresado=int(input("Ingrese Valor a Convertir : "))

Val_Binario=''
while Numero_Ingresado != 0:

         if (Numero_Ingresado%2)==0:
             Val_Binario=Val_Binario+'0'
         else:
            Val_Binario=Val_Binario+'1'

         Numero_Ingresado=Numero_Ingresado//2


largo_Binario=len(Val_Binario)-1
i=largo_Binario
Val_Binario_fin=''
while i >=0:
        Val_Binario_fin=Val_Binario_fin+Val_Binario[i]
        ##print(Val_Binario_fin)
        ##print(i)

        i=i-1
print("resultado=", Val_Binario_fin)