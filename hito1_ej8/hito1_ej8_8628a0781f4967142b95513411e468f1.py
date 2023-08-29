#Descomponer un número
numero = int(input("ingrese un numero de hasta cuatro digitos:"))
mil = int(numero/1000)
resto = int(numero-(mil*1000))
cen = int(resto/100)
restodos = int(resto-(cen*100))
dec = int(restodos/10)
uni = int(restodos-(dec*10))
print(mil,"M +",cen,"C +",dec,"D +",uni,"U ")  