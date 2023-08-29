#Contestador de celular
Tel=int(input())
Hora=int(input())
if Hora<7:
    print("CONTESTAR")
elif Hora<14:
    Tela=Tel/1000
    Telb=int(Tela)
    Telc=Telb*1000
    Teld=Tel-Telc
    if Teld==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<Hora<19:
    Tela=Tel/100000
    Telb=int(Tela)
    if Telb==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif Hora>19:
    print("NO CONTESTAR")     