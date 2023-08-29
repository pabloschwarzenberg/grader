#Descomponer un número
n = int(input("ingresar un numero:"))
millon = (n//1000)
cen = (n -(millon*1000))//100
dec = (n - (millon*1000 + cen*100))//10
uni = n - (millon*1000 + cen*100 + dec*10)
print(millon,"M","+" ,cen ,"C","+" ,dec ,"D" ,"+" ,uni, "U")