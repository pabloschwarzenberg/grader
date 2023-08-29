#Descomponer un número
NUMERO = int(input("Ingresa un numero natural de 1,2,3 o 4 cifras:"))
if NUMERO>0:
    MIL = NUMERO//1000
    CENTENA = (NUMERO%1000)//100
    DECENA = ((NUMERO%1000)%100)//10
    UNIDAD = ((NUMERO%1000)%100)%10
    print(str(MIL)+"M+"+str(CENTENA)+"C+"+str(DECENA)+"D+"+str(UNIDAD)+"U")

else:
     print("Tiene que ser un numero de hasta 4 cifras.")