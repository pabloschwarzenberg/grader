#Descomponer un número
numero= int(input("Ingrese un nÚmero de cuatro dÍgitos:"))
uni= numero%10
dec= int((numero/10)%10)
cen= int((numero/100)%10)
mil= int((numero/1000)%10)
print('El número descompuesto es: ',str(mil)+,'M +',str(cen)+,'C +',str(dec)+,'D +',str(uni)+,'U')
