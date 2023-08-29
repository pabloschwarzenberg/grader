numero = float (input ("Ingrese numero a binarizar:"))
binario = " "
num = numero
while num // 2 != 0:
        binario = str(round(num % 2))+binario
        num = num // 2
final = str (round (num))+binario
print ("resultado=",int(final))
