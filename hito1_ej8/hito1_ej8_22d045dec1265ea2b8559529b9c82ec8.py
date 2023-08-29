#Descomponer un número
numero = int(input("Ingrese un numero de hasta 4 cifras:"))
d1 = numero%10
numero = numero//10
d2 = numero%10
numero = numero//10
d3 = numero%10
numero = numero//10
d4 = numero%10
numero = numero//10
if 1 <= 9:
    cadenadecaracteres = str(d1)+"U"
    print(cadenadecaracteres)
if 10 <= 99:
    cadenadecaracteres = str(d2)+"D +"+ str(d1)+"U"
    print(cadenadecaracteres)
if 100 <= 999:
    cadenadecaracteres = str(d3)+"C +"+str(d2)+"D +"+str(d1)+"U"
    print(cadenadecaracteres)
if 1000 <= 9999:
    cadenadecaracteres = str(d4)+"M +"+str(d3)+"C +"+str(d2)+"D +"+str(d1)+"U"
    print(cadenadecaracteres)