#Contestador de celular
numero=int(input())
hora=int(input())
termino=numero%1000
inicio=numero//100000
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora<14 and termino==909:
    print("CONTESTAR")
elif hora<14 and termino!=909:
    print("NO CONTESTAR")
elif hora>=17 and hora<=19 and inicio!=877:
    print("CONTESTAR")
elif hora>=17 and hora<=19 and inicio==877:
    print("NO CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")