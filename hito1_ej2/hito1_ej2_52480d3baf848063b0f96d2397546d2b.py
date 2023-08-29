#Contestador de celular
print("Introduce el numero telefonico")
numero = int(input())
print("Introduce la hora de la llamada")
hora = float(input())

ocho = numero % 10
numero = numero // 10

siete = numero % 10
numero = numero // 10

seis = numero % 10
numero = numero // 10

cinco = numero % 10
numero = numero // 10

cuatro = numero % 10
numero = numero // 10

tres = numero % 10
numero = numero // 10

dos = numero % 10
numero = numero // 10

uno = numero % 10
numero = numero // 10

while hora in range(7):
    print("CONTESTAR")
    break
while hora in range(14):
    if(ocho == 9 and siete == 0 and seis == 9):
        print("CONTESTAR")
        break
    else:
        print("NO CONTESTAR")
        break
while hora in range(17, 19):
    if(uno == 8 and dos == 7 and tres == 7):
        print("NO CONTESTAR")
        break
    else:
        print("CONTESTAR")
        break
while hora in range(19, 24):
    print("NO CONTESTAR")
    break