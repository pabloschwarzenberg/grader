num = int(input("Ingrese Número de 4 Cifras : "))
cen = num//100%10
dec = num//10%10
uni = num%10
mil = num//1000%10
print(str(mil)+ 'M+' + str(cen)+ 'C+' + str(dec)+ 'D+' + str(uni)+ 'U')
