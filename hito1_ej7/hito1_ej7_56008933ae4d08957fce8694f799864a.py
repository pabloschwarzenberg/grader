D=input("Ingrese día del cumpleaños: ")
D=int(D)
M=input("Ingrese mes del cumpleaños: ")
M=int(M)
if M==3 and 21<=D or M==4 and D<=20:
        print("Aires")
elif M==4 and 21<=D or M==5 and D<=21:
        print("Tauro")
elif M==5 and 22<=D or M==6 and D<=21:
        print("Geminis")
        
elif M==6 and 22<=D or M==7 and D<=22:
        print("Cancer")
elif M==7 and 23<=D or M==8 and D<=22:
        print("Leo")
elif M==8 and 23<=D or M==9 and D<=22:
        print("Virgo")
elif M==9 and 23<=D or M==10 and D<=22:
        print("Libra")
elif M==10 and 23<=D or M==11 and D<=21:
        print("Escorpio")
elif M==11 and 22<=D or M==12 and D<=21:
        print("Sagitario")
elif M==12 and 22<=D or M==1 and D<=20:
        print("Capricornio")
elif M==1 and 21<=D or M==2 and D<=19:
        print("Acuario")
elif M==2 and 19<=D or M==3 and D<=20:
        print("Piscis")

      