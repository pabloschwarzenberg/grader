#Entrada
Numero = int(input("Escriba un numero de 4 digitos: "))
Num = str(Numero)

#Descomposicion del Num

M = Num[0]
C = Num[1]
D = Num[2]
U = Num[3]
if M and C  and D  and U :
    print('f'{M}''M +'f'{C}''C +'f'{D}''D +'f'{U}'U')
