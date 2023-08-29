#Conversión de Decimal a Binario
      
a = int(input("Ingrese Numero: "))
lista = []
stringLindo = ""

while a!=0:
    if (a==1):
        #print("1")
        lista.append("1")
        break

    else:
        if (a%2==0):
            binar=0
            a= a//2
            lista.append(str(binar))
                   
        else:
            binar=1
            a= a//2
            lista.append(str(binar))
print(lista)
lista.reverse()
print(lista)

for binario in lista:
    stringLindo = stringLindo+binario

print("resultado="+stringLindo)