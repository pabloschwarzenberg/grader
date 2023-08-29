
dia = int(input("Ingrese dia de cumpleaños")) 
mes = int(input("Ingrese mes de cumpleaños")) 


if mes == 1:
  if dia >= 20 and dia <= 31:
    print("acuario")
  elif dia <= 19 and dia >= 1:
    print("capricornio")

elif mes == 2:
  if dia <= 19:
    print("acuario")
  elif dia >= 20:
    print("piscis")  

elif mes == 3:
  if dia <= 21:
    print("piscis") 
  elif dia >= 22:  
    print("aries")

elif mes == 4:
  if dia <= 20:
    print("aries")
  elif dia >= 21:
    print("tauro")   

elif mes == 5:
  if dia <= 21:
    print("tauro")   
  elif dia >= 22:
    print("geminis")
     
elif mes == 6:
  if dia <= 21:
    print("geminis")
  elif dia >= 22:
    print("cancer")  

elif mes == 7:
  if dia <= 23:
    print("cancer") 
  elif dia >= 24:
    print("leo")  

elif mes == 8:
  if dia <= 23:
    print("leo")  
  elif dia >= 24:
    print("virgo")  

elif mes == 9:
  if dia <= 23:
    print("virgo")  
  elif dia >= 24:
    print("libra") 

elif mes == 10:
  if dia <= 23:
    print("libra")  
  elif dia >= 24:
    print("escorpio") 

elif mes == 11:
  if dia <= 22:
    print("escorpio")  
  elif dia >= 23:
    print("sagitario") 

elif mes == 12:
  if dia <= 22:
    print("sagitario")  
  elif dia >= 23:
    print("capricornio")
 
     