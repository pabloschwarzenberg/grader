#Contestador de celular
telefono=int(input())
horario=int(input())
if horario>=0 and horario<=7:
    print("CONTESTAR")
elif horario>7 and horario<14:
    if telefono%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif horario>=14 and horario<=19:
    if telefono//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    if horario>19 and horario<23:
        print("NO CONTESTAR")