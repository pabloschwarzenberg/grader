#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos: "))
unidades=(numero//1%10)
decenas=(numero//10%10)
centenas=(numero//100%10)
u_miles=(numero//1000%10)
print("U",unidades)
print("D",decenas)
print("C",centenas)
print("M",u_miles )
print(u_miles,("M"),("+"),centenas,("C"),("+"),decenas,("D"),("+"),unidades,("U"))