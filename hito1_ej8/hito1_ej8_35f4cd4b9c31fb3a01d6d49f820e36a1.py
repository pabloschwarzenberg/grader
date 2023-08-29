#Descomponer un numero
num = eval(input("introduce un numero de 4 digitos: "))
uni= num%10
num = num//10
dece = num%10
num = num//10
cen = num%10
num = num//10
uni_m = num%10

print(uni_m,"M +",cen,"C +",dece,"D +",uni,"U")