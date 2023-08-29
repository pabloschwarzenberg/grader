#Conversión de Decimal a Binario
numero=int(input("Ingrese numero:"))
numb=""
while numero>0:
    if numero%2==0:
        numb=str(0)+numb
    else:
        numb=str(1)+numb
    numero=numero//2
print("Resultado=",numb)      