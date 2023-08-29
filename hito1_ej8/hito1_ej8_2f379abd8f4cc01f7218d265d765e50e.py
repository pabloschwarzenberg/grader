#Entrada
Num = str(input("Escriba un numero: "))

#Descomposicion del Num
x = len(Num)



#calculo de num
if x == 4:
    M = Num[0]
    C = Num[1]
    D = Num[2]
    U = Num[3]
    if M and C  and D  and U:
        print(M + 'M + ' + C + 'C + '+ D +'D + '+ U +'U')
elif x == 3:
    M = Num[0]
    C = Num[1]
    D = Num[2]
    if M  and C  and D:
        print(M +'C + '+ C +'D + '+ D +'U')
elif x == 2:
    M = Num[0]
    C = Num[1]
    if M  and C:
        print(M +'D + '+ C +'U')
elif x == 1:
    M = Num[0]
    if M:
        print(M +' U')
else:
    print('Los digitos ingresados no corresponden con lo pedido')