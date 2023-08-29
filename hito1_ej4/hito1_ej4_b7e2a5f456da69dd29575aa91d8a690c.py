#Conversión de Decimal a Binario
Num_decimal=int(input("Ingrese un número decimal: "))
lista=[]
while Num_decimal>=1:
  lista.insert(0,Num_decimal%2)
  Num_decimal=Num_decimal // 2
Resultado= "".join(str(i) for i in lista)
print('Resultado= ',Resultado)