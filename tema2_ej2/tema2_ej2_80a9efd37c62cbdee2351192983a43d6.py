num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))

def amigos(num1):
    n = []
    x = 0
    b = 0
    for i in range(1,num1):
        if (num1%i) == 0:
            n.append(i)
    for i in n:
        x+=n[b]
        b+=1
    return x
def amigos2(num2):
    k =[]
    y = 0
    c = 0
    for j in range(1,num2):
        if (num2%j) == 0:
            k.append(j)
    for j in k:
        y+=k[c]
        c+=1
    return y

if amigos2(num2) == num1:
     print(True)
elif amigos(num1) == num2:
    print(True)
else:
     print(False)