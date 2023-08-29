#Descomponer un número
num=int(input("Número natural de 1 a 4 espacios: "))
if 0<num<10000:
    Miles=num//1000
    Centena=(num%1000)//100
    Decena=((num%1000)%100)//10
    Unidad=((num%1000)%100)%10
    print(Miles,"M +",Centena,"C +",Decena,"D +",Unidad,"U")
else:
    print("Debe ser un número de hasta 4 espacios")     