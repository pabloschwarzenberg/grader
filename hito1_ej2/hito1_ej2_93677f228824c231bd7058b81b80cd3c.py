#Contestador de celular
print("Introducir numero telefonico")
num = int(input())
print("Introducir hora de la llamada")
hora = float(input())

ocho = num % 10
num = num // 10
siete = num % 10
num = num // 10
seis = num % 10
num = num // 10
cinco = num % 10
num = num // 10
cuatro = num % 10
num = num // 10
tres = num % 10
num = num // 10
dos = num % 10
num = num // 10
uno = num % 10
num = num // 10

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