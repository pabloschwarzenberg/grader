#Descomponer un número
#Entrada
num=int(input("Introduzca un número de hasta 4 dígitos: "))

if num>=0 and num<= 9999:
    if num >= 1000 and  num <= 9999:
        dig1= num // 1000
        
        dig2= num % 1000
        dig2= dig2 // 100
        
        dig3= num // 10
        dig3= dig3 % 10
        
        dig4= num % 10
        print(str(dig1)+ "M", "+", str(dig2)+ "C","+", str(dig3)+ "D","+", str(dig4)+ "U")
        
    elif num >= 100 and num <= 999:
        dig1= num // 100
        
        dig2= num % 100
        dig2= dig2 // 10

        dig3= num % 10
        print(str(dig1)+ "C", "+", str(dig2)+ "D","+", str(dig3)+ "U")
        
    elif num>=10 and num <=99:
        dig1= num // 10
        
        dig2= num %10
        print(str(dig1)+ "D", "+", str(dig2)+ "U")
        
    else:
        print(str(num) + "U")

else:
    print("El número introducidos posee más de 4 cifras")      