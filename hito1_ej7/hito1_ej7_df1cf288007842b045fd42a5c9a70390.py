#Zodiaco
dia = int(input())
mes = int(input())

if (mes == 3 and dia >= 21) or (mes == 4 and dia < 20):
    print("Aries")
    
elif (mes == 4 and dia >= 20) or (mes == 5 and dia < 21):
    print("Taurus")

elif (mes == 5 and dia >= 21) or (mes == 6 and dia < 21):
    print("Gemini")
    
elif (mes == 6 and dia >= 21) or (mes == 7 and dia < 23):
    print("Cancer")
    
elif (mes == 7 and dia >= 23) or (mes == 8 and dia < 23):
    print("Leo")

elif (mes == 8 and dia >= 23) or (mes == 9 and dia < 23):
    print("Virgo")
    
elif (mes == 9 and dia >= 23) or (mes == 10 and dia < 23):
    print("Libra")
    
elif (mes == 10 and dia >= 23) or (mes == 11 and dia < 23):
    print("Scorpio")
    
elif (mes == 11 and dia >= 23) or (mes == 12 and dia < 22):
    print("Sagittario")
    
elif (mes == 12 and dia >= 22) or (mes == 1 and dia < 20):
    print("Capricorn")
    
elif (mes == 1 and dia >= 20) or (mes == 2 and dia < 21):
    print("Aquarius")
    
else:
    print("Piscis")