decimal = int(input("decimal: "))
bits = 1
binario = ""

while True:
    if (2** bits) -1 >= decimal:
        break
    bits= bits +1

i = bits -1
suma = 0
while i >= 0:
    if suma + (2** i) <= decimal:
        binario = binario + "1"
        suma= suma + 2** i
    else:
        binario = binario + "0"
    i= i -1

print ("resultado=", binario)
