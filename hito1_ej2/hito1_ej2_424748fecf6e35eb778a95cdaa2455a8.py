#Contestador de celular
a=input('ingrese numero de telefono:')
b=input('ingrese la hora actual:')
b=int(b)
x=a[5:8]
y=a[0:4]
x=int(x)
y=int(y)
if b >= 0 and b <= 7:
    print('contestar')
elif b <=14 and b > 7 and x!=909:
    print('no contestar')
elif b <=14 and b > 7 and x==909:
    print('contestar')
elif b > 14 and b < 17 :
    print('no contestar')
elif b >= 17 and b <= 19 and y!=877:
    print('no contestar')
elif b >= 17 and b <= 19 and y==877:
    print('contestar')
elif b >= 19 :
    print('no contestar')