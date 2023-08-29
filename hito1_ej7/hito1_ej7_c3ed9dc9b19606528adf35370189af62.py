#Zodiaco
dia=int(input())
mes=int(input())
if (dia>=21 and mes==3) or (dia<21 and mes==4):
  print("aries")
else:
  if (dia>=21 and mes==4) or (dia<22 and mes==5):
    print("tauro")
  else:
    if (dia>=22 and mes==5) or (dia<22 and mes==6):
      print("geminis")
    else:
      if (dia>=22 and mes==6) or (dia<23 and mes==7):
        print("cancer")    
      else:
        if (dia>=23 and mes==7) or (dia<23 and mes==8):
          print("leo")
        else:
          if (dia>=23 and mes==8) or (dia<24 and mes==9):
            print("virgo")
          else:
            if (dia>=24 and mes==9) or (dia<24 and mes==10):
              print("libra")
            else:
              if (dia>=24 and mes==10) or (dia <23 and mes==11):
                print("escorpio")
              else:
                if (dia>=23 and mes==11) or (dia<22 and mes==12):
                  print("sagitario")
                else:
                  if(dia>=22 and mes==12) or (dia<21 and mes==1):
                    print("capricornio")
                  else:
                    if(dia>=21 and mes==1) or (dia<20 and mes==2):
                      print("acuario")
                    else:
                      print("piscis")