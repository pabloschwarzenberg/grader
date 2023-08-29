#Contestador de celular
numero=int(input())
hora=int(input())

if 0<= hora <= 7:
    print("CONTESTAR")

if 7 < hora <= 14 and numero % 1000 == 909:
        print("CONTESTAR")


elif 17 <= hora <=19 and numero // 100000 == 877:
        print("NO CONTESTAR")

elif 17 < hora <= 19:
    print("CONTESTAR")



else:
    print("NO CONTESTAR")