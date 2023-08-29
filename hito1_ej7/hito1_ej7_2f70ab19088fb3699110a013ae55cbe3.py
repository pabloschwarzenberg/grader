#Zodiaco
d = eval(input("Ingrese su dia de nacimiento: "))
m = eval(input("Ingrese su mes de nacimiento: "))

if (m==3 and 21<=d<=31) or (m==4 and 21>d>=1):
    print("aries")
elif(m==4 and 21<=d<=30) or (m==5 and 21>d>=1): 
    print("tauro")
elif(m==5 and 21<=d<=31) or (m==6 and 21>d>=1): 
    print("geminis")
elif (m==6 and 21<=d<=30) or (m==7 and 23>d>=1):
    print("cancer")
elif(m==7 and 21<=d<=31) or (m==8 and 21>d>=1): 
    print("leon")
elif (m==8 and 21<=d<=30) or (m==9 and 21>d>=1):
    print("virgo")    
elif (m==9 and 21<=d<=30) or (m==10 and 21>d>=1):
    print("libra")
elif(m==10 and 21<=d<=31) or (m==11 and 22>d>=1):  
    print("escorpion")
elif (m==11 and 21<=d<=30) or (m==12 and 22>d>=1):
    print("sagitario")
elif (m==12 and 21<=d<=31) or (m==1 and 20>d>=1):
    print("capricornio")
elif (m==1 and 21<=d<=31) or (m==2 and 19>d>=1):
    print("acuario")
elif (m==2 and 21<=d<=28) or (m==3 and 21>d>=1):
    print("piscis")
