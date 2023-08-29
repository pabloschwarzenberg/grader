numero = eval(input("ingresa un numero natural de 4 cifras como maximo \n "))

if numero > 0:
    miles = numero // 1000
    centena = (numero % 1000) // 100
    decena = ((numero % 1000) % 100) // 10
    unidad = ((numero % 1000) % 100) % 10
    print(str(miles)+"M+"+str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U")

else:
     print("tu numero tiene que ser de 4 cifras como maximo")