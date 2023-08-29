#Descomponer un número
P = int(input("elige un numero natural de 1,2,3 o 4 digitos:"))
if 0<P<10000:
    m = P//1000
    Centena = (P%1000)//100
    Decena = ((P%1000)%100)//10
    Unidad = ((P%1000)%100)%10
    print(str(m)+"M + "+str(Centena)+"C + "+str(Decena)+"D + "+str(Unidad)+"U")
else:
     print("Debe ser un numero de hasta 4 digitos")