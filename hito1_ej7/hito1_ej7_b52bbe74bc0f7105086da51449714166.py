#Zodiaco
D=int(input("dia de nacimiento:"))
M=int(input("mes de nacimiento:"))

if 21<=D<=31 and M==3 or 1<=D<=20 and M==4:
    print("aries")
elif 21<=D<=30 and M==4 or 1<=D<=21 and M==5:
    print("taurus")
elif 22<=D<=31 and M==5 or 1<=D<=21 and M==6:
    print("gemini")
elif 22<=D<=30 and M==6 or 1<=D<=22 and M==7:
    print("cancer")
elif 23<=D<=31 and M==7 or 1<=D<=22 and M==8:
    print("leo")
elif 23<=D<=31 and M==8 or 1<=D<=23 and M==9:   
    print("virgo")       
elif 24<=D<=30 and M==9 or 1<=D<=23 and M==10:   
    print("libra")           
elif 24<=D<=31 and M==10 or 1<=D<=22 and M==11:   
    print("escorpio")           
elif 23<=D<=30 and M==11 or 1<=D<=21 and M==12:   
    print("sagitario")       
elif 22<=D<=31 and M==12 or 1<=D<=20 and M==1:   
    print("capricorn")           
elif 21<=D<=31 and M==1 or 1<=D<=19 and M==2:   
    print("aquarius") 
elif 20<=D<=28 and M==2 or 1<=D<=20 and M==3:  
    print("piscis") 
