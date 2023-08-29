#Descomponer un número
numero=int(input("numero: "))
unidad=numero%10
decena=(numero%100-numero%10)//10
centena=(numero%1000-numero%100)//100
milesima=(numero%10000-numero%1000)//1000
print(milesima,"M + ",centena,"C + ",decena,"D + ",unidad,"U")