#Contestador de celular
numero_tel = input("ingrese el numero: ")
horario = input("ingrese la hora: ")

if horario >= "20":
    print("no contestar")
elif horario >= "17" or horario <= "19" and numero_tel[5:120] == "877":
    print("no contestar")
elif horario >= "17" or horario <= "19":
    print("contestar")
elif horario <= "14" and numero_tel[5:120] == "909":
    print("contestar")
elif horario >= "0" or horario <= "7":
    print("contestar")