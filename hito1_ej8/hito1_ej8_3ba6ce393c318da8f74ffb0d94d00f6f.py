
    
num = int(input("ingrese un numero de 4 digitos"))


unidades = num%10
decenas = int((num/10)%10)
centenas = int((num/100)%10)
miles = int((num/1000)%10)
print("El numero descompuesto es:",str(miles)+"M + "+ str(centenas)+"C +" + str(decenas)+"D+" + str(unidades)+"U")

