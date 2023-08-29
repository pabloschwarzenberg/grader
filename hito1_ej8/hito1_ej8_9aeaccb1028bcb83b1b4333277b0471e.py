#Descomponer un número
nmb = int(input("Ingrese un numero,el cual puede ser de 1,2,3 o 4 cifras:"))
if nmb>0:
    udemil = nmb//1000
    centena = (nmb%1000)//100
    decena = ((nmb%1000)%100)//10
    unidad = ((nmb%1000)%100)%10
    print(str(udemil)+"M+"+str(centena)+"C+"+str(decena)+"D+"+str(unidad)+"U")

else:
     print("Debe ser un numero de hasta 4 cifras")