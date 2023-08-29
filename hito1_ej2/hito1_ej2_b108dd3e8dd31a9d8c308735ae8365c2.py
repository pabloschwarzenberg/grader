#Contestador de celular
a=int(input("ingrese numero telefonico:"))
b=int(input("ingrese hora de la llamada:"))

c=a%1000
d=a%100000
e=a-d
f=e/100000

if 0 <= b <= 7:
    print('CONTESTAR')
elif 8 <= b <= 14 and c == 909:
    print('CONTESTAR')
elif 8 <= b <= 14:
    print('NO CONTESTAR')
elif 17 <= b <= 19 and f == 877:
    print('NO CONTESTAR')
elif 17 <= b <= 19:
    print('CONTESTAR')
elif 19 <= b <= 23:
    print('NO CONTESTAR')
