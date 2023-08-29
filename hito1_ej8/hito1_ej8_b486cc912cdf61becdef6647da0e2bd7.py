numero=int(input("escriba un numero de 4 digitos "))
milesima=numero//1000
centena=numero//100%10
decena=numero//10%10
unidad=numero%10
print(milesima,"M","+",centena,"C","+",decena,"D","+",unidad,"U")