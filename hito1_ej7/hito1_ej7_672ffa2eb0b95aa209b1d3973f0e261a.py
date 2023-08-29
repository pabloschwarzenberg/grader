dia = int(input("ingrese el dia de nacimiento: "))
mes = int(input("ingrese el mes de nacimiento: "))

if 21 <= dia <= 31 and mes == 3 or 1 <= dia <= 20  and mes == 4:
  print("Aries")
elif 20 <= dia <= 31 and mes == 4 or 1 <= dia <= 21  and mes == 5:
    print("tauro")
elif 21 <= dia <= 31 and mes == 4 or 1 <= dia <= 21  and mes == 6:
    print("geminis")
elif 21 <= dia <= 31 and mes == 4 or 1 <= dia <= 23  and mes == 7:
    print("cancer")
elif 23 <= dia <= 31 and mes == 4 or 1 <= dia <= 23  and mes == 8:
    print("leo")
elif 23 <= dia <= 31 and mes == 4 or 1 <= dia <= 23  and mes == 9:
    print("virgo")
elif 23 <= dia <= 31 and mes == 4 or 1 <= dia <= 23  and mes == 10:
    print("libra")
elif 23 <= dia <= 31 and mes == 4 or 1 <= dia <= 22  and mes == 11:
    print("escorpio")
elif 23 <= dia <= 31 and mes == 4 or 1 <= dia <= 22  and mes == 12:
    print("sagitario")
elif 22 <= dia <= 31 and mes == 4 or 1 <= dia <= 20  and mes == 1:
    print("capricornio")
elif 20 <= dia <= 31 and mes == 4 or 1 <= dia <= 19  and mes == 2:
    print("acuario")
elif 21 <= dia <= 31 and mes == 4 or 1 <= dia <= 21  and mes == 3:
    print("piscis")
else:
    print("ingrese una dia y mes valido")