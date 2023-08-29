hora=int(input("Ingrese la hora:"))
te= int(input("Ingrese el numero telefonico:"))
#909
ul= te-((te//10**3)*10**3)
pr=(te//10**5)

if  7>= hora >= 0:
    print("CONTESTAR")
else:
    if ((hora<14) or (ul==909)):
        print ("CONTESTAR")
    else: 
        if (pr==877):
            print("NO CONTESTAR")
        else:
            if (17 >=hora and hora <=19):
                print("CONTESTAR")
            else:
                if hora>=19:
                    print("NO CONTESTAR")