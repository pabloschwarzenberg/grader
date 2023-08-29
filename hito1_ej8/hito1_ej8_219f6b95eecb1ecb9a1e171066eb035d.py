#Descomponer un número
num = int(input("Número natural de hasta 4 cifras: "))
if 0<num<10000:
    un_de_mil = num//1000
    cent = (num%1000)//100
    dec = ((num%1000)%100)//10
    uni = ((num%1000)%100)%10
    print(un_de_mil,"M +",cent,"C +",dec,"D +",uni,"U")
else:
    print("Debe ser un número de hasta 4 cifras")