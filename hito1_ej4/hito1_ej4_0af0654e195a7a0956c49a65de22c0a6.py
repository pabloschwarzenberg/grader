n = int(input("Escriba el numero"))
binario = ""
while n != 0:
    m = n/2
    m1 = int(m)
    m2 = float(m)
    if m1==m2:
        binario = "0" + binario
        n = int (m)
    else:
        binario = "1" + binario
        n = int (m)

print("resultado=",binario)



