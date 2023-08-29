#Descomponer un número
numero = int(input("numero natural de 1,2,3 o 4 cifras:"))
if numero>0:
    mil = numero//1000
    centena = (numero%1000)//100
    decena = ((numero%1000)%100)//10
    unidad = ((numero%1000)%100)%10
    print(str(mil)+"M+"+str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U")

else:
     print("debe ser un numero de hasta 4 cifras")     