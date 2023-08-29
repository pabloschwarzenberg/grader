#Entrada
num = input("Ingrese un numero hasta 4 digitos: ")
valor = int(num)
#asd
if len(num) <= 4:
    M = valor // 1000
    valor -= M * 1000
    C = valor // 100
    valor -= C * 100
    D = valor // 10
    valor -= D * 10
    U = valor
    valor = int(num)
    if valor >= 1000:
        print(str(M)+"M+"+str(C)+"C+"+str(D)+"D+"+str(U)+"U")
    elif valor >= 100:
        print(str(C)+"C+"+str(D)+"D+"+str(U)+"U")
    elif valor >= 10:
        print(str(D)+"D+"+str(U)+"U")
    elif valor >= 1:
        print(str(U)+"U")
    else:
        print("0U")