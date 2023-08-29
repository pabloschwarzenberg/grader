#Contestador de celular
numero=int(input("numero: "))
hora=int(input("hora: "))
fin_num=(numero%1000)
com_num=(numero//100000)
if hora>=0  and hora<=7:
    print ("CONTESTAR")
    
elif hora>=8  and hora<=14:
    if fin_num!=909:
        print ("NO CONTESTAR")
    elif fin_num==909:
        print ("CONTESTAR")
         
elif hora>17  and hora<19:
    if com_num==877:
        print ("NO CONTESTAR")
    elif com_num!=877:
        print ("CONTESTAR")
else:
    print ("NO CONTESTAR")      