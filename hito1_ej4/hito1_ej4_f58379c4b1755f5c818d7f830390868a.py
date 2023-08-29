dec = int(input())
binario = 0
mult = 0
while dec > 0:
    num  = dec%2
    dec = int(dec//2)
    binario = binario + num * (10**mult)
    mult = mult + 1
print("resultado=",binario)