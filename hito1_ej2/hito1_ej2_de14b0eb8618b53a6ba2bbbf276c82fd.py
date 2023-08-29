#Contestador de celular
numero=int(input())
hora=int(input())
if 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<=14 and numero%1000==909:
    print("CONTESTAR")
elif 17<=hora<=19 :
    if numero//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif 19<hora :
    print("NO CONTESTAR")   