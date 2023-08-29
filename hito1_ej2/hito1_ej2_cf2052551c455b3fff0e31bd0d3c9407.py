num = input("Ingrese numero telefonico: ")
hrs = input("Ingrese hora de la llamada: ")
i = 8

resultado = [int(a) for a in str(num)]
if i > len(resultado):
    print('NUMERO INVALIDO')
    exit()

ult3 = str(resultado[5]) + str(resultado[6]) + str(resultado[7])


if 0 <= int(hrs) <= 7:
    print("CONTESTAR")

elif int(hrs) > 14 and ult3 != "909":
    print("NO CONTESTAR")

elif 17 < int(hrs) < 19 and ult != "877":
    print('CONTESTAR')

elif int(hrs) > 19:
    print("NO CONTESTAR")

else:
    print("CONTESTAR")
