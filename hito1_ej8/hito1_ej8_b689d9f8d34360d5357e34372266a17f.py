#Descomponer un número
num = int(input("numero natural de 1,2,3 o 4 cifras:"))
if num>0:
    mil = num//1000
    centena = (num%1000)//100
    decena = ((num%1000)%100)//10
    unidad = ((num%1000)%100)%10
    print(str(mil)+"M+"+str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U")
    
else:
     print("debe ser un numero de hasta 4 cifras")