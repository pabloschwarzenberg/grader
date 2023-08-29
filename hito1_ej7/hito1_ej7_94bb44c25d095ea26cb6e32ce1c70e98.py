#Zodiaco
dia = int(input("¿Qué día naciste?: "))
mes = int(input("¿En qué mes naciste?, escribelo en números: "))
 
if((mes == 1 and dia >= 20) or (mes == 2 and dia <= 19)):
    print("Eres acuario")
elif((mes == 2 and dia >= 19) or (mes == 3 and dia <= 21)):
    print("Eres piscis")
elif((mes == 3 and dia >= 21) or (mes == 4 and dia <= 20)):
    print("Eres aries")
elif((mes == 4 and dia >= 20) or (mes == 5 and dia <= 21)):
    print("Eres tauro")
elif((mes == 5 and dia >= 21) or (mes == 6 and dia <= 21)):
    print("Eres geminis") 
elif((mes == 6 and dia >= 21) or (mes == 7 and dia <= 23)):
    print("Eres cancer")
elif((mes == 7 and dia >= 23) or (mes == 8 and dia <= 23)):
    print("Eres leo") 
elif((mes == 8 and dia >= 23) or (mes == 9 and dia <= 23)):
    print("Eres virgo")
elif((mes == 9 and dia >= 23) or (mes == 10 and dia <= 23)):
    print("Eres libra")  
elif((mes == 10 and dia >= 23) or (mes == 11 and dia <= 22)):
    print("Eres escorpio")  
elif((mes == 11 and dia >= 23) or (mes == 12 and dia <= 22)):
    print("Eres sagitario")   
elif((mes == 12 and dia >= 22) or (mes == 1 and dia <= 20)):
    print("Eres capricornio")