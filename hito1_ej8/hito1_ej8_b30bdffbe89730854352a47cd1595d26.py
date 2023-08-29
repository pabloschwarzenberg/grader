#Descomponer un número
num=int(input("ingrese un número entero de hasta 4 digitos: "))
salida=""
if (num//1000)>0:
    salida=salida+str(num//1000)+"M + "
    num=num%1000
if (num//100)>0:
    salida=salida+str(num//100)+"C + "
    num=num%100
if (num//10)>0:
    salida=salida+str(num//10)+"D + "
    num=num%10
if num>0:
    salida=salida+str(num)+"U"

print(salida)     