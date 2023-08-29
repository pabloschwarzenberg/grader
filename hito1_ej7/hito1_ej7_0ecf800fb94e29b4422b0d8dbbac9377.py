#Zodiaco
DN=int(input("ingrese su dia de nacimiento: "))
MN=int(input("ingrese su mes de nacimiento: "))
signo=["Capricornio","Acuario","Picis","Aries","Tauro","Geminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario"]
fecha=[20,19,20,21,21,22,22,22,22,22,21,22]
MN=MN-1
if(DN>fecha[MN]):
  MN=MN+1
if(MN==12):
  MN=0
print("Su signo zodiacal es:",signo[MN])