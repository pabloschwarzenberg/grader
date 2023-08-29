#Descomponer un número
Num = int(input("Numero natural de 1,2,3 o 4 cifras:"))
if Num>0:
    Mil = Num//1000
    Centena = (Num%1000)//100
    Decena = ((Num%1000)%100)//10
    Unidad = ((Num%1000)%100)%10
    print(str(Mil)+"M+"+str(Centena)+"C+"+str(Decena)+"D+"+str(Unidad)+"U")
    
else:
     print("Debe ser un numero de hasta 4 cifras")      