#Descomponer un número
num = int(input("Ingrese numero de 4 digitos : "  ))

udemil = num // 1000
c = num //100 - (num //1000)*10
d = num //10 - (num //100)*10
u = num //1 - (num//10)*10

print( udemil,"M +" , c ,"C +", d ,"D +" , u , "U " )