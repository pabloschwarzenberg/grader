#Zodiaco
dia_naci = int(input("Ingresar día de nacimiento: "))
mes_naci = int(input("Ingresar mes de nacimiento: "))

#Ecuación
if (dia_naci >= 21 and mes_naci == 3) or (dia_naci <= 20 and mes_naci == 4):
    print ("aries")
elif (dia_naci >= 21 and mes_naci == 4) or (dia_naci <= 20 and mes_naci == 5):
    print ("tauro")
elif (dia_naci >= 21 and mes_naci == 5) or (dia_naci <= 20 and mes_naci == 6):
    print ("geminis")
elif (dia_naci >= 21 and mes_naci == 6) or (dia_naci <= 20 and mes_naci == 7):
    print ("cancer")
elif (dia_naci >= 21 and mes_naci == 7) or (dia_naci <= 20 and mes_naci == 8):
    print("leo")
elif (dia_naci >= 21 and mes_naci == 8) or (dia_naci <= 20 and mes_naci == 9):
    print ("virgo")
elif (dia_naci >= 21 and mes_naci == 9) or (dia_naci <= 20 and mes_naci == 10):
    print("libra")
elif (dia_naci >= 21 and mes_naci == 10) or (dia_naci <= 20 and mes_naci == 11):
    print("escorpio")
elif (dia_naci >= 21 and mes_naci == 11) or (dia_naci <= 20 and mes_naci == 12):
    print("sagitario")
elif (dia_naci >= 21 and mes_naci == 12) or (dia_naci <= 20 and mes_naci == 1):
    print("capricornio")
elif (dia_naci >= 21 and mes_naci == 1) or (dia_naci <= 20 and mes_naci == 2):
    print("acuario")
else:
    print("piscis")