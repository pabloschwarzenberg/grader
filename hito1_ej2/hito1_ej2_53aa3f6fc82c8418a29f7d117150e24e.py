#Contestador de celular
a=input('ingrese numero:')
b=int(input('ingrese hora:'))
c=int(str(a)[-3]+str(a)[-2]+str(a)[-1])
d=int(str(a)[0]+str(a)[1]+str(a)[2])
if(b<=7 and b>=0):
    print('CONTESTAR')
elif(b<14 and c==909):
    print('CONTESTAR')
elif(b<14):
    print('NO CONTESTAR')
elif(b<=19 and b>=17 and d==877):
    print('NO CONTESTAR')
elif(b<=19 and b>=17):
    print('CONTESTAR')
elif(b>19):
    print('NO CONTESTAR')      