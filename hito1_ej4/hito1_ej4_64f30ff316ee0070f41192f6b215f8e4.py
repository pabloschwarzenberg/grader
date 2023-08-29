numero=int(input("Ingrese Numero: "))

binario=''
while numero != 0:

         if (numero%2)==0:
             binario=binario+'0'
         else:
            binario=binario+'1'

         numero=numero//2


largo_Binario=len(binario)-1
i=largo_Binario
Binario2=''
while i >=0:
        Binario2=Binario2+binario[i]
        ##print(Binario2)
        ##print(i)

        i=i-1
print("resultado=", Binario2)
