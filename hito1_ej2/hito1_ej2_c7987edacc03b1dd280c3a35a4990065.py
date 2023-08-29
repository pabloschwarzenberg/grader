numerotelefonico = int(input("ingrese numero telefonico: "))
horallamada = int(input("ingrese hora llamada: "))

final = numerotelefonico % 1000
inicio= numerotelefonico // 100000

if horallamada >= 0 and horallamada <= 7:
    print("contestar")

elif horallamada <=13 and final == 909:
    print("contestar")
elif horallamada <=13:
    print("no contestar")

elif horallamada >= 17 and horallamada <=19 and inicio == 877:
    print(" no contestar")
elif horallamada >= 17 and horallamada <=19:
    print("contestar")

elif horallamada >=19:
    print("no contestar")


