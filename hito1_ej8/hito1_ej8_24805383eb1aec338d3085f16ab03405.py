#Descomponer un número
num = int(input("Ingresa un digito de 4 cifras"))
mil = num//1000
cen = num %1000 // 100
dec = num % 100 // 10
uni = num %10

print (str(mil)+ "M+" + str(cen) +"C+" + str(dec) + "D+" + str(uni) + "U")
