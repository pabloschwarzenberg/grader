#Descomponer un número
numero=eval(input('ingrese numero : '))
unidades=numero%10
decenas=(numero%100-unidades)//10
centenas=(numero%1000-(decenas*10))//100
miles= (numero -(centenas*100))//1000
if (numero>999):
 print(miles,"M+",centenas,"C+",decenas,"D+",unidades,"U")
elif (numero>99):
 print(centenas,"C+",decenas,"D+",unidades,"U")
elif (numero>9):
 print(decenas,"D+",unidades,"U")
else:
 print(unidades,"U")