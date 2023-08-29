#Descomponer un número
#ENTRADA 
num = int(input("Ingrese Número de 1 A 4 Cifras : "))

#PROCESAMIENTO
mil = num//1000
cen = (num%1000)//100
res = num%100
dec = (res-(res%10))//10
uni = res%10

#SALIDA
print(mil,"M + ",end = ""), 
print(cen,"C + ",end = ""),
print(dec,"D + ",end = ""),
print(uni,"U")      