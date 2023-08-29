telefono=int(input("nùmero de teléfono: "))
hora=int(input("hora: "))
if(0<=hora<=6):
    print("CONTESTAR")
if(7<=hora<=13):
    if(telefono%1000==909):
        print("CONTESTAR")
    if(telefono%1000!=909):
        print("NO CONTESTAR")
if(17<=hora<=18):
     if(telefono//100000==877):
                print("NO CONTESTAR")
     if(telefono//100000!=877):
                print("NO CONTESTAR")
if((14<=hora<=16) or (19<=hora<=23)):
    print("NO CONTESTAR")

