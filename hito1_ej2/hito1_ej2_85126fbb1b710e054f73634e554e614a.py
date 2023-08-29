#Contestador de celular
numero= int(input("numero llamando: "))
hora = int(input("hora del dia: "))
if 0<=hora<=7:
    print("CONTESTAR")
elif hora<14 and numero%1000==909:
    print("CONTESTAR")
elif 17<=hora<=19 and numero//100000==877:
    print("NO CONTESTAR")
elif 17<=hora<=19:
    print("CONTESTAR")
elif 19<hora:
    print("NO CONTESTAR")
else: print("NO CONTESTAR")