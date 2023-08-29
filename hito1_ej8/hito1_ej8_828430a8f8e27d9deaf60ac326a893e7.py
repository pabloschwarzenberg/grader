numero=eval(input('ingrese numero: '))
uni=numero%10
decenas=(numero%100-uni)//10
centenas=(numero%1000-(decenas*10))//100
miles= (numero -(centenas*100))//1000
if (numero>999):
 print(miles,'M+',centenas,'C+',decenas,'D+',uni,'U')
elif (numero>99):
 print(centenas,'C+',decenas,'D+',uni,'U')
elif (numero>9):
 print(decenas,'D+',uni,'U')
else:
 print(unidades,'U')