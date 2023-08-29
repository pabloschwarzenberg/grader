#Zodiaco
dia=int(input("ingrese su dia de nacimiento:"))
mes=int(input("ingrese su mes de nacimiento:"))

if ((21<=dia and 3==mes) or (dia<=20 and 4==mes)):
   print("Aries")
elif ((21<=dia and 4==mes) or (dia<=21 and 5==mes)):
   print("Tauro")
elif ((22<=dia and 5==mes) or (dia<=21 and 6==mes)):
   print("Geminis")
elif ((22<=dia and 6==mes) or (dia<=22 and 7==mes)):
   print("Cancer")
elif ((23<=dia and 7==mes) or (dia<=22 and 8==mes)):
   print("Leo")
elif ((23<=dia and 8==mes) or (dia<=23 and 9==mes)):
   print("Virgo")
elif ((24<=dia and 9==mes) or (dia<=23 and 10==mes)):
   print("Libra")
elif ((24<=dia and 10==mes) or (dia<=22 and 11==mes)):
   print("Escorpio")
elif ((23<=dia and 11==mes) or (dia<=21 and 12==mes)):
   print("Sagitario")
elif ((22<=dia and 12==mes) or (dia<=20 and 1==mes)):
   print("Capricornio")
elif ((21<=dia and 1==mes) or (dia<=19 and 2==mes)):
   print("Acuario")
elif ((20<=dia and 2==mes) or (dia<=20 and 3==mes)):
   print("Piscis")
