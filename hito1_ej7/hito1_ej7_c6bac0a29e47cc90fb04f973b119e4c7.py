#Zodiaco
N = int(input("Ingrese un numero entero \n"))
M = input("Ingrese un mes \n")
if (M=="marzo" and N>=21) or (M=="abril" and N<=20):

   print("Aries")
   elif (M=="abril" and N>=21) or (M=="mayo" and N<=20):
   print("Tauro")
   elif (M=="mayo" and N>=21) or (M=="junio" and N<=21):
   print("Geminis")
   elif (M=="junio" and N>=22) or (M=="julio" and N<=22):
   print("Cancer")
   elif (M=="julio" and N>=23) or (M=="agosto" and N<=23):
   print("Leo")
   elif (M=="agosto" and N>=24) or (M=="septiembre" and N<=23):
   print("Virgo")
   elif (M=="septiembre" and N>=24) or (M=="octubre" and N<=23):
   print("Libra")
   elif (M=="octubre" and N>=23) or (M=="noviembre" and N<=22):
   print("Escorpio")
   elif (M=="noviembre" and N>=23) or (M=="diciembre" and N<=21):
   print("Sagitario")
   elif (M=="diciembre" and N>=22) or (M=="enero" and N<=19):
   print("Capricornio")
   elif (M=="enero" and N>=20) or (M=="febrero" and N<=19):
   print("Acuario")
   elif (M=="febrero" and N>=20) or (M=="marzo" and N<=20):
   print("Piscis")