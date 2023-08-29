#Descomponer un número
N = int(input("ingrese numero de hasta 4 digitos:"))
mil = int (N/1000)
cen = int ((N - (mil*1000))/100)
dec = int ((N - (mil*1000 + cen*100))/10)
unidad = int ((N -(mil*1000 + cen*100 + dec*10)))
a = str (mil)
b = str (cen)
c = str(dec)
d = str(unidad)
print(a +"M+"+ b +"C+"+ c +"D+"+ d +"U")

