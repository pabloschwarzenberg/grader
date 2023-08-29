#Descomponer un número
numero = int(input("Ingrese en numero:"))
tmpnumero=numero
dig=int(0)
suma=0;
while(tmpnumero!=0):
    dig=int(tmpnumero % 10)
    suma+=dig
    tmpnumero=int(tmpnumero/10)
print("La suma de los digitos de ",numero," es ",suma)     