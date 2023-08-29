#Descomponer un número
n=int(input(""))
milesima_n=(n//1000)
centena_n=((n%1000)//100)
decena_n=(((n%1000)%100)//10)
unidad_n=(((n%1000)%100)%10)
if milesima_n==0 and centena_n!=0:
    print(centena_n,"C +",decena_n,"D +",unidad_n,"U")
if milesima_n==0 and centena_n==0 and decena_n!=0:
    print(decena_n,"D +",unidad_n,"U")
if milesima_n==0 and centena_n==0 and decena_n==0:
    print(unidad_n,"U")
if milesima_n>0 and centena_n>0 and decena_n>=0 and unidad_n>=0:
    print(milesima_n,"M +",centena_n,"C +",decena_n,"D +",unidad_n,"U")   