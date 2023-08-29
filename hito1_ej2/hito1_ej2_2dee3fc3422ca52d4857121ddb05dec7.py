call=True
tel=input("inserte el telefono: ")
hora=int(input("Indique la bora: "))
a="877"
ltel=len(tel)-1
if((hora<=7) and (hora>=0)):
    print("CONTESTAR")
elif(hora>=7 and hora<=14 and (str(tel[ltel]+tel[ltel-1]+tel[ltel-2])=="909")):
    print("CONTESTAR")
elif(hora>=7 and hora<=14):
    print("NO CONTESTAR")
elif((hora>=17 and hora<=19) and str(tel[0]+tel[1]+tel[2])==a):
    print("NO CONTESTAR")
elif(hora>=17 and hora<=19):
    print("CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")