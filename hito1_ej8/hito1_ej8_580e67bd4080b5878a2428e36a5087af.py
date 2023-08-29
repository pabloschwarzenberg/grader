numero = []
numero = input("Introduce un numero\n")

if(len(numero) == 1):
    print(numero, "U")
elif(len(numero) == 2):
    decenas = int(numero) / 10
    unidades = int(numero) % 10
    print(int(decenas), "D +" ,unidades, "U")
elif(len(numero) == 3):
    centenas = int(numero) / 100
    r = int(numero) % 100
    decenas = r / 10
    unidades = r % 10
    print(int(centenas), "C +", int(decenas), "D +" ,unidades, "U")
elif(len(numero) == 4):
    miles = int(numero) / 1000
    r = int(numero) % 1000
    centenas = r / 100
    r = r % 100
    decenas = r / 10
    unidades = r % 10
    print(int(miles), "M +", int(centenas), "C +", int(decenas), "D +" ,int(unidades), "U")
else:
    print("El numero debe de ser de 4 digitos")