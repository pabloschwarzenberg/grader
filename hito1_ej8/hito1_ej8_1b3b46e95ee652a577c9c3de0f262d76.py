#Descomponer un número
A = int(input("numero de hasta 4 cifras: "))
if 0<A<10000:
    Mil = A//1000
    Centena = (A%1000)//100
    Decena = ((A%1000)%100)//10
    Unidad = (((A%1000)%100)%10)%10
    print(Mil,"M + ",Centena," C + ",Decena," D + ",Unidad,"U")
else:
    print("EXCEDE LA CANTIDAD DE CIFRAS PERMITIDAS")