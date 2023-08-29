#Contestador de celular
numero=input(":")
horario=int(input(":"))
if horario>=0 and horario<=7:
    print("Contestar")
elif numero[5:]=="909":
    print("Contestar")
elif numero[:3]!="877" and (horario>=17 and horario<=19):
    print("Contestar")
else:
    print("No contestar")