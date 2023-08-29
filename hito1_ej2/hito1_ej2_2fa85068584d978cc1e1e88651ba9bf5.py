#Contestador de celular
#Contestador de celular
#NumTel=input('ingrese numero telefonico (8 digitos):\t')
#Hora=input('ingrese hora (0 - 23):\t\t')
Lista=[input('ingrese numero telefonico (8 digitos):\t'),input('ingrese hora (0 - 23):\t\t')]
#print(Lista[0],'\t',int(Lista[1]))
LenNumTel=len(Lista[0])
PL1=(LenNumTel==8)and(0<=int(Lista[1])<=23)
EvalNum=(int(Lista[0])/10000000)
PL2=(0<EvalNum<10)
PL3=(PL1 and PL2)
#print('Prueba Logica 1:\t{}\nPruena Logica 2:\t{}'.format(PL1, PL2))

while True:
    Ult3Num=str(Lista[0])[5:8]
    #print(Ult3Num)
    Pri3Num=str(Lista[0])[0:3]
    #print(Pri3Num)
    if (PL3 is True):
        if 0<=int(Lista[1])<=7:
            print('CONTESTAR')
            break
        elif 7<int(Lista[1])<=14 and Ult3Num!='909':
            print('NO CONTESTAR')
            break
        elif 7<int(Lista[1])<=14 and Ult3Num=='909':
            print('CONTESTAR')
            break
        elif 17<int(Lista[1])<19 and Pri3Num!='877':
            print('CONTESTAR')
            break
        elif 17<int(Lista[1])<19 and Pri3Num=='877':
            print('NO CONTESTAR')
            break
        elif int(Lista[1])>=19:
            print('NO CONTESTAR')
            break
        else:
            break
    else:
        print('INFORMACIÓN INVALIDA')
        break
     