#Zodiaco



sign = ("capricornio", "acuario", "piscis", "aries", "tauro", "geminis", "cancer", "LEO", "virgo", "libra", "escorpion", "sagitario")
limit = ( 20, 19, 20, 20, 21, 21, 22, 22, 23, 22, 22, 21)
 
dia=input("Escriba su dia: ")
dia=int (dia)
  
coso=input("Escriba su mes: ")
coso=int (coso)
 
coso=coso-1;
if (dia>limit[coso]):
    coso=coso+1
 
if (coso==12):
    coso=0
print (sign[coso])