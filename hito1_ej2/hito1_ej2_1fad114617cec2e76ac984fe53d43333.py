telefono=int(input("telefono"))
hora=int(input("hora"))
if hora>0 and hora<7:
    print("CONTESTAR")
elif hora>=7 and hora<14:
    if telefono%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>=14 and hora<=19:
    if hora>17 and hora<19 and telefono//100000!=877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")      