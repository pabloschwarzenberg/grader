#Conversión de Decimal a Binario
num = []
num1 = []
bi = []
numero = int(input("Ingrese numero a transformar: "))
i = 0
txt = ""
while True:
    des = 2 ** i
    if numero > des:
        i+=1
    elif numero == des:
        num1.append(des)
        num.append(i)
        numero = numero - des
        break
    elif numero < des:
        i = i - 1
        des = 2**i
        num.append(i)
        num1.append(des)
        numero = numero - des
        i = 0
    elif numero == 0:
        break
    elif numero == 1:
        num.append(0)
        break
i = max(num)
while True:
    des = 2**i
    if des in num1:
        bi.append(1)
        i-=1
        if i == -1:
            break
    else:
        bi.append(0)
        i-=1
        if i == -1:
            break
for a in range(len(bi)):
    if a != (len(bi) - 1):
        txt += str(bi[a])
    else:
        txt += str(bi[a])
print(txt)
    