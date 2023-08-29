#Descomponer un número
numero=(input("Ingresa Número de hasta 4 Digitos:"))
nConverNum=str(numero)
nNum=len(numero)


while  (nNum<1) or (nNum>4) :
    numero=(input("Ingresa Número de hasta 4 Digitos:"))
    nConverNum=str(numero)
    nNum=len(numero)
    
if nNum==4:
    unidad=nConverNum[3]
    decena=nConverNum[2]
    centena=nConverNum[1]
    miles=nConverNum[0]
    print(miles,"M +",centena,"C +", decena,"D +" ,unidad,"U")

if nNum==3:
    unidad=nConverNum[2]
    decena=nConverNum[1]
    centena=nConverNum[0]
    print(centena,"C +", decena,"D +" ,unidad,"U")
if nNum==2:
    unidad=nConverNum[1]
    decena=nConverNum[0]
    print(decena,"D +" ,unidad,"U")

if nNum==1:
    unidad=nConverNum[0]
    print(unidad,"U")
