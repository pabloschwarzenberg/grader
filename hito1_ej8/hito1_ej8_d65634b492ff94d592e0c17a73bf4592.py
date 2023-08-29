#Descomponer un número
numero = int(input(' Introduzca un numero max 4 numeros :'))

m = numero // 10
c = numero % 1000
d = numero % 100
u = numero % 10
df = d // 10
cf = c // 100
mf = m // 100


    
if (mf > 0 and cf > 0):
    print(mf,"M","+",cf,"C","+",df,"D","+",u,"U")
if (mf == 0 and cf > 0):
    print(cf,"C","+",df,"D","+",u,"U")
if (mf == 0 and cf == 0):
    print(df,"D","+",u,"U")
