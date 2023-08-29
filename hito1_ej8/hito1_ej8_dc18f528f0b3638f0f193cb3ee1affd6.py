#Descomponer un número
numero = input("Ingrese el N° a descomponer, tamaño max 4 digitos")
aula = True
if(len(numero) > 4 ):
    print("Error, el max es de 4 digitos")
    aula= False
    exit()
millares=int(numero)/1000
centenas=(int(numero)-(int(millares)*1000))/100
decenas=(int(numero)- (int(millares)*1000 + int(centenas)*100))/10
unidades=int(numero)-(int(millares)*1000 + int(centenas)*100 + int(decenas)*10 )
millar = ""
cent = ""
dece = ""
uni = ""
if(int(millares) != 0):
    millar = (int(millares))
    millar = str(millar) + "M + "

if(int(centenas) != 0 ):
    cent = int(centenas)
    cent = str(cent) + "C + "

if(int(decenas) != 0):
    dece = int(decenas)
    dece = str(dece) + "D + "


uni = int(unidades)
uni = str(uni) + "U"

print(millar + cent + dece + uni)      