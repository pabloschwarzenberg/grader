#Contestador de celular
NT = int(input("Ingrese su número telefonico de 8 digitos: "))
H = int(input("INgrese la hora de la llamada: "))
if (00<=H<=7):
    print("No contestar")
elif ((NT % 1000) == 909) and (8<=H<=14):
    print("Contestar")
elif 8<=H<=14:
    print("No contestar")
elif ((NT // 100000) == 877) and (17<=H<=19):
    print("No contestar")
elif 17<=H<=19:
    print("Contestar")
elif 19<H<=23:
    print("No contestar")      