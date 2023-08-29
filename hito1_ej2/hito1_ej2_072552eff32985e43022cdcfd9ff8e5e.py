#Contestador de celular
num=int(input("Ingrese número de teléfono: "))
hora=int(input("Ingrese hora de la llamada: "))
a=num//10000000
aa=a%10
b=num//1000000
bb=b%10
c=num//100000
cc=c%10
f=num//100
ff=f%10
g=num//10
gg=g%10
h=num//1
hh=h%10
if 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<=14 and ff!=9 and gg!=0 and hh!=9:
    print("NO CONTESTAR")
elif 7<hora<=14 and ff==9 and gg==0 and hh==9:
    print("CONTESTAR")
elif 14<hora<=17 or 19<hora<=23:
    print("NO CONTESTAR")
elif 17<hora<=19 and aa==8 and bb==7 and cc==7:
    print("NO CONTESTAR")
elif 17<hora<=19 and aa!=8 and bb!=7 and cc!=7:
    print("CONTESTAR")
