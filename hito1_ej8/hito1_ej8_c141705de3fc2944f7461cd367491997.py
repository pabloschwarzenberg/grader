#Descomponer un número
numero= int(input("ingrese un numero de cuatro digitos:"))      
uni= numero%10
dec= int((numero/10)%10)
cen= int((numero/100)%10)
mil= int((numero/1000)%10)
print("el numero descompuesto es:",str(mil)+"M +",str(cen)+"C +",str(dec)+"D +",str(uni)+"U")