#Contestador de celular
numero=int(input('Ingrese el numero telefonico: '))
hora=int(input('Hora de la llamada : '))
a=numero%10
b=(numero//10)%10
c=(numero//100)%10
d=(numero//1000)%10
e=(numero//10000)%10
f=(numero//100000)%10
g=(numero//1000000)%10
h=(numero//10000000)%10
if 0 <=hora <=7:
    print('CONTESTAR')
elif 8 <=hora <= 14 and c != 9 and b != 0 and a != 9:
    print('NO CONTESTAR')
elif 8<= hora <= 14 and c == 9 and b == 0 and a == 9:
    print('CONTESTAR')
elif 15 <= hora <= 16:
    print('NO CONTESTAR')
elif 17 <= hora <= 19 and h != 8 and g != 7 and f != 7:
    print('CONTESTAR')
elif 17 <= hora <= 19 and h == 8 and g == 7 and f == 7:
    print('NO CONTESTAR')
elif 20 <= hora <= 23:
    print('NO CONTESTAR')   
