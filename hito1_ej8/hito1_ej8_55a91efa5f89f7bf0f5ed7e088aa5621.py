#Descomponer un número
numero = int(input("Ingresa un numero de hasta 4 digitos: "))
salva = numero
d1 = numero%10
numero = numero // 10
d2 = numero%10
numero = numero // 10
d3 = numero%10
numero = numero // 10
d4 = numero%10
numero = numero // 10

if salva < 10000:    
    if 0 <= salva < 10:
        Digitos= str(d1)+ "U"
    elif 10 <= salva < 100:
        Digitos =  str(d2) + "D" + "+" + str(d1) + "U"
    elif 100 <= salva < 1000:
        Digitos =  str(d3) + "C" + "+" + str(d2) + "D" + "+" + str(d1) + "U"
    elif 1000 <= salva < 10000:
        Digitos =  str(d4) + "M" + "+" + str(d3) + "C" + "+" + str(d2) + "D" + "+" + str(d1) + "U"
    print(Digitos)
else:
    print("Número Invalido")
      