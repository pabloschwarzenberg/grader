#Descomponer un número
num = int(input("Ingrese un número de hasta 4 dígitos:"))
miles = int(num/1000)
cen = int((num-(miles*1000))/100)
dec = int((num-(miles*1000 + cen*100))/10)
uni = int((num-(miles*1000 + cen*100 + dec*10)))
a = str(miles)
b = str(cen)
c = str(dec)
d = str(uni)
print(a+"M +"+b+"C +"+c+"D +"+d+"U")