#Descomponer un número
num = (input("Ingrese un numero :"))
Contador = len(str(num))
if Contador == 4:
    Miles = num[0:1]
    Centena = num[1:2]
    Decena = num[2:3]
    Unidad = num[3:4]
    print(Miles+"M+"+Centena+"C+"+Decena+"D+"+Unidad+"U")
elif Contador == 3:
    Centena = num[0:1]
    Decena = num[1:2]
    Unidad = num[2:3]
    print(Centena+"C+"+Decena+"D+"+Unidad+"U")
elif Contador == 2:
    Decena = num[0:1]
    Unidad = num[1:2]
    print(Decena+"D+"+Unidad+"U")
elif Contador == 1:
    Uni = num[0:1]
    print(Unidad+"U")
  