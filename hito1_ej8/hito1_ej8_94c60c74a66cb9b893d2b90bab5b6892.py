#Descomponer un número
print("MOSTRAR LA UNIDAD, LA DECENA, CENTENA Y MILES.")
num = int(input("Ingrese Un Número de hasta 4 Cifras : "))
mil = (num-(num%100))/1000
res = num%1000    
cen = (res-(num%100))/100
res = num%100
dec = (res-(res%10))/10
uni = res%10
print(int (mil),"M +",int(cen),"C +",int(dec),"D +",int(uni),"U ")




 