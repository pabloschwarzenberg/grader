#Zodiaco
d=int(input("Ingrese dia de nacimiento:"))
m=int(input("Ingrese mes de nacimiento:"))
while (d<=0 or d>31 ):
    d=int(input("Número incorrecto,ingrese día de nacimiento: "))
 
while(m<=0 or m>12):
    m=int(input("Número incorrecto,ingrese mes de nacimiento: "))
    
#Aries    
if((m==3 and d>20) or (m==4 and d<21)):
   print("ARIES")
#Tauro 
elif ((m==4 and d>20) or (m==5 and d<22)):
   print("TAURO")
#Geminis
elif ((m==5 and d>21) or (m==6 and d<22)):
   print("GEMINIS")
#Cancer 
elif ((m==6 and d>21) or (m==7 and d<23)):
   print("CANCER")
#Leo 
elif ((m==7 and d>22) or (m==8 and d<23)):
   print("LEO")
#Virgo 
elif ((m==8 and d>22) or (m==9 and d<24)):
   print("VIRGO")
#Libra 
elif ((m==9 and d>23) or (m==10 and d<24)):
   print("LIBRA")
#Escorpion 
elif ((m==10 and d>23) or (m==11 and d<23)):
   print("ESCORPION")
#Sagitario 
elif ((m==11 and d>22) or (m==12 and d<22)):
   print("SAGITARIO")
#Capricornio 
elif ((m==12 and d>21) or (m==1 and d<21)):
   print("CAPRICORNIO")   
#Acuario 
elif ((m==1 and d>20) or (m==2 and d<20)):
   print("ACUARIO")
#Piscis
elif ((m==2 and d>19) or (m==3 and d<21)):
   print("PISCIS")   
    