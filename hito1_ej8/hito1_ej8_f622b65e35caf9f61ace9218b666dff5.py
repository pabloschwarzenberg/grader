#Descomponer un número
rut = int(input())
dig1= rut%10
dig2= (rut//10)%10
dig3= (rut//100)%10
dig4= (rut//1000)%10

if rut>99:
    print(dig4,"M +",dig3,"C +",dig2,"D +",dig1,"U")
else:
    print(dig2,"D +",dig1,"U")    