#Zodiaco
dia=int(input("Ingrese el día de su cumpleagnos: "))
mes=int(input("Ingrese el mes de su cumpleagnos: "))

if(((21<=dia<=31)and(mes==3))or((1<=dia<=20)and(mes==4))):
    print("Aries")
else:
    if(((21<=dia<=30)and(mes==4))or((1<=dia<=21)and(mes==5))):
        print("Tauro")
    else:
        if(((22<=dia<=31)and(mes==5))or((1<=dia<=21)and(mes==6))):
            print("Geminis")
        else:
            if(((22<=dia<=30)and(mes==6))or((1<=dia<=22)and(mes==7))):
                print("Cáncer")
            else:
                if(((23<=dia<=31)and(mes==7))or((1<=dia<=22)and(mes==8))):
                    print("Leo")
                else:
                    if(((23<=dia<=31)and(mes==8))or((1<=dia<=23)and(mes==9))):
                        print("Virgo")
                    else:
                        if(((24<=dia<=30)and(mes==9))or((1<=dia<=23)and(mes==10))):
                            print("Libra")
                        else:
                            if(((24<=dia<=31)and(mes==10))or((1<=dia<=22)and(mes==11))):
                                print("Escorpión")
                            else:
                                if(((23<=dia<=30)and(mes==11))or((1<=dia<=21)and(mes==12))):
                                    print("Sagitario")
                                else:
                                    if(((22<=dia<=31)and(mes==12))or((1<=dia<=20)and(mes==1))):
                                        print("Capricornio")
                                    else:
                                        if(((21<=dia<=31)and(mes==1))or((1<=dia<=19)and(mes==2))):
                                            print("Acuario")
                                        else:
                                            print("Piscis")     