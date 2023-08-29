#Descomponer un número
print("10. MOSTRAR LA UNIDAD, LA DECENA Y CENTENA.")
num = int(input("Ingrese Un Número de hasta 4 Cifras : "))
mil = (num-(num%100))/1000
res1 = num%1000
cen = (res1-(res1%10))/100
res = num%100
dec = (res-(res%10))/10
uni = res%10
print(int(mil),"M","+",int(cen),"C","+",int(dec),"D","+",int(uni),"U")