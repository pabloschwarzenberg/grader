#Zodiaco
d= int(input("ingrese el dia de nacimiento:"))
m= int(input("ingrese el mes de nacimiento:"))
if (m == 3 and d > 21) or (m == 4 and d <= 20) :     
 print("ARIES") 
elif (m == 4 and d > 20) or (m == 5 and d <= 21) :
 print("TAURO")    
if (m == 5 and d > 21) or (m == 6 and d <= 21) :
 print("GEMINIS")    
elif (m == 6 and d > 21) or (m == 7 and d <= 23) :
 print("CANCER")   
if (m == 7 and d > 23) or (m == 8 and d <= 23) :
 print("LEO")   
elif (m == 8 and d > 23) or (m == 9 and d <= 23) :
 print("VIRGO")     
if (m == 9 and d > 23) or (m == 10 and d <= 23):  
 print("LIBRA")
elif (m == 10 and d > 23) or (m == 11 and d <= 22) :
 print("ESCORPIO")
if (m == 11 and d > 23) or (m == 12 and d <= 22) :
 print("SAGITARIO")
elif (m == 12 and d > 22) or (m == 1 and d <= 20) :
 print("CAPRICORNIO")
if (m == 1 and d > 20) or (m == 2 and d <= 19) :
 print("ACUARIO")
elif (m == 2 and d > 19) or (m == 3 and d <= 21) :
 print("PISCIS")     