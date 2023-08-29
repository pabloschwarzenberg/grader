#Descomponer un número
n = int(input("número: "))
miles = n//1000
centenas = (n//100)%10
decenas = (n//10)%10
unidades = n%10
if miles == 0 and centenas == 0 and decenas == 0:
    print(unidades,"U")
elif miles == 0 and centenas == 0:
    print(decenas,"D +",unidades,"U")
elif miles == 0:
    print(centenas,"C + ",decenas,"D + ",unidades,"U")  
else:
    print(miles,"M + ",centenas,"C + ",decenas,"D + ",unidades,"U")    