#Contestador de celular
n = int(input("ingrese el numero telefonico:"))
H = int(input("debe ser representada entre un numero entre 0 y 23"))
d8 = n//10000000
rest = (n%10000000)
n = rest
d7 = n//1000000
rest = (n%1000000)
n = rest
d6 = n//100000
n = (n%100000)
n = rest
d5 = n//10000
rest = (n%10000)
n = rest
d4 = n//1000
rest = (n%1000)
n = rest
d3 = n//100
rest = (n%100)
n = rest
d2 = n//10
rest = (n%10)
n = rest
d1 = rest
if 7>H>0:
    print("CONTESTAR")
elif 14>H and d1==9 and d2==0 and d3==9:
    print("CONTESTAR")
elif 14>H:
    print("NO CONTESTAS")
elif 19>H>17 and d8==8 and d7==7 and d6==7:
    print("NO CONTESTAR")
elif 19>H>17:
    print("CONTESTAR")
elif H>19:
    print("NO CONTESTAR")    