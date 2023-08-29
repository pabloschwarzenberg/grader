N = input("Ingrese un numero: ")
H = int(input("Ingrese la hora, ejemplo: 15: "))
if H >= 0 and H <= 7:
    print("Contestar")
elif H > 7 and H < 14 and N[5] == "9" and N[6] == "0" and N[7] == "9":
    print("Contestar")
elif H > 7 and H < 14:
    print("No contestar")
elif H > 17 and H < 19 and N[0] == "8" and N[1] == "7" and N[2] == "7":
    print("No contestar")
elif H > 17 and H < 19:
    print("Contestar")
elif H > 19:
    print("No contestar")