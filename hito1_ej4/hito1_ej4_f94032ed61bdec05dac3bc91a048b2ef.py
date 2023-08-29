#Conversión de Decimal a Binario
Z = int(input("ingrese numero: ")) 
Num_decimal = Z
modulos = [] 
bin=""
cont = 0
while Num_decimal != 0: 

    Modulo = Num_decimal % 2
    Cociente = Num_decimal // 2
    modulos.append(Modulo) 
    Num_decimal = Cociente 
    cont=cont+1
while cont != 0:
  bin=bin+str(modulos[cont-1])
  cont=cont-1
res = "resultado=" + bin
str.strip(res)
print(res)