#Zodiaco
dia= int(input())
mes= int(input())
if (mes == 1 and 1 <= dia <= 20) or (mes== 12 and 22 <= dia <= 31):
 print("capricornio")
elif (mes== 4 and 21<=dia<=30) or (mes==5 and 1<=dia<=20) : 
  print("tauro")
elif (mes==5 and 21<=dia<=31) or (mes==6 and 1<=dia<=20):
   print("geminis")
elif (mes == 6 and 21 < dia < 30) or (mes== 7 and 1 <= dia <= 22):
    print("cancer")
elif (mes== 7 and 23<=dia<=31) or (mes==8 and 1<=dia<=22) : 
   print("leo")
elif (mes==8 and 23<=dia<=31) or (mes==9 and 1<=dia<=22) :
    print("virgo")
elif (mes == 9 and 23 <= dia <= 30) or (mes== 10 and 1 <= dia <= 22):
     print("libra")
elif (mes== 10 and 23<=dia<=31) or (mes==11 and 1<=dia<=22) : 
      print("escorpio")
elif (mes==11 and 23<=dia<=30) or (mes==12 and 1<=dia<=21) :
       print("sagitario")
elif (mes==1 and 22<=dia<=31) or (mes==2 and 1<=dia<=21) :
        print("acuario")
elif (mes == 2 and 22 <= dia <= 28) or (mes== 3 and 1 <= dia <= 23):
         print("piscis")
elif (mes== 3 and 24<=dia<=31) or (mes==4 and 1<=dia<=20) : 
          print("aries")