#Descomponer un número
num = int(input("Ingrese un numero"))

millon= (num//1000)
centenas=(num - ( millon* 1000))//100
decenas= (num - (millon*1000 + centenas*100))//10
unidad= num -(millon *1000 + centenas * 100 + decenas *10)

print (millon,"M", "+", centenas, "C", "+", decenas, "D", "+", unidad, "U")