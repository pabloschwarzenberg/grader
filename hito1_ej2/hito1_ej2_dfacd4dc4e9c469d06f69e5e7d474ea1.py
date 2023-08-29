#Contestador de celular
numero=int(input('Ingrese numero telefonico: '))
hora=int(input('Ingrese hora de la llamada: '))

b=numero//1000
ult_numero=numero-b*1000
com_numero=numero//100000

if 0<=hora<=7 :
    print('Resultado: CONTESTAR')
elif (8<=hora<=14 and ult_numero==909) :
    print('Resultado: CONTESTAR')
elif (17<=hora<=19 and com_numero!=877) :
    print('Resultado: CONTESTAR')
else :
    print('Resultado: NO CONTESTAR')