#Descomponer un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))
if numero < 0 or numero > 9999:
    print("Número inválido. Por favor, ingrese un número entre 0 y 9999.")
else:
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000

if numero < 9:
    print (unidades, "U")
    
elif  numero < 100:
    print (decenas ,"D +" , unidades, "U") 

elif  numero < 1000:
    print(centenas, "C + " ,decenas ,"D + ", unidades, "U")

elif  numero < 10000:
    print(miles, "M +" ,centenas, "C + " ,decenas ,"D + ", unidades, "U")