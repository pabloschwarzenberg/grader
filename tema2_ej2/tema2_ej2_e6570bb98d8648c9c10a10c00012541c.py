print("Numeros Amigos ")
Numero_1=int(input("Ingrese Numero 1: "))
Numero_2=int(input("Ingrese Numero 2: "))
Suma_divisor_1=Suma_divisor_2=0
x=1
while x<Numero_1 :
    if Numero_1 % x == 0 :
        Suma_divisor_1+=x
    x+=1
y=1
while y<Numero_2 :
    if Numero_2 % y == 0 :
        Suma_divisor_2+=y
    y+=1
print("Sumas son:", Suma_divisor_1,Suma_divisor_2)
if Suma_divisor_1 ==  Numero_2 and Suma_divisor_2==Numero_1:         