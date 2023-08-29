#Descomponer un número
num = int(input("Ingresa un número de 4 cifras: "))
mil = num / 1000
res = num % 1000
cen = res / 100
res = res % 100
dec = res / 10
uni = res % 10
print("\n")
print("Descompisicón: ",int(mil),"M + ",int(cen),"C + ",int(dec),"D + ",int(uni),"U")