numPhone = int(input("Ingrese el número de teléfono"))
timeCall = int(input("Ingrese la hora de llamada"))
numPhoneString = str(numPhone)


if(len(numPhoneString)==8 and timeCall >=0 and timeCall <=23 ):
    if(timeCall>0 and timeCall<7):
        print("CONTESTAR")

    elif(timeCall>=7 and timeCall<14):
        if(numPhoneString[-3:]== "909"):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")

    elif(timeCall>=14 and timeCall<17):
            print("NO CONTESTAR")

    elif(timeCall>=17 and timeCall<19):
        if(numPhoneString[0:3]== "877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")

    elif(timeCall>=19):
            print("NO CONTESTAR")