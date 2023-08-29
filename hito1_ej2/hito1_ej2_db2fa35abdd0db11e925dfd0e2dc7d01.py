#Contestador de celular
numero=int(input("Número que llama: "))
hora=int(input("Hora de la llamada: "))
if 0<=hora<=7:
    print("CONTESTAR")
elif 8<=hora<=13 and numero%1000==909:
    print("CONTESTAR")
elif 8<=hora<=13:
    print("NO CONTESTAR")
elif 14<=hora<=16:
    print("NO CONTESTAR")
elif 17<=hora<=19 and numero//100000==877:
    print("NO CONTESTAR")
elif 17<=hora<=19:
    print("CONTESTAR")
elif 20<=hora<=23:
    print("NO CONTESTAR")















