day = int (input("Ingresa el día en que naciste: "))
month = int (input("Ingresa tu mes de nacimiento (como número): "))

if day in range(21 , 32) and month == int(3) or day in range(0 , 20) and month == int(4):
    print ("Tú eres Aries")
if day in range(21 , 32) and month == int(4) or day in range(0 , 21) and month == int(5):
    print ("Tú eres Tauro")
if day in range(22 , 32) and month == int(5) or day in range(0 , 21) and month == int(6):
    print ("Tú eres Geminis")
if day in range(22 , 32) and month == int(6) or day in range(0 , 23) and month == int(7):
    print ("Tú eres Cancer")
if day in range(24 , 32) and month == int(7) or day in range(0 , 23) and month == int(8):
    print ("Tú eres Leo")
if day in range(24 , 32) and month == int(8) or day in range(0 , 23) and month == int(9):
    print ("Tú eres Virgo")
if day in range(24 , 32) and month == int(9) or day in range(0 , 23) and month == int(10):
    print ("Tú eres Libra")
if day in range(24 , 32) and month == int(10) or day in range(0 , 22) and month == int(11):
    print ("Tú eres Escorpion")
if day in range(23 , 32) and month == int(11) or day in range(0 , 22) and month == int(12):
    print ("Tú eres Sagitario")
if day in range(23 , 32) and month == int(12) or day in range(0 , 20) and month == int(1):
    print ("Tú eres Capricornio")
if day in range(21 , 32) and month == int(1) or day in range(0 , 19) and month == int(2):
    print ("Tú eres Acuario")
if day in range(20 , 32) and month == int(2) or day in range(0 , 21) and month == int(3):
    print ("Tú eres Piscis")
else:
    print ("ERROR! Reinicia el programa y pon números correctos")