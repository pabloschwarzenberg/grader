celu= int(input("ingrese numero celu:"))
tiempo=int(input("ingrese numero de hora:"))

comienzo = celu//100000

final = celu%1000
if tiempo>=0 and tiempo<=7:
    print("CONTESTAR")
elif tiempo>7 and tiempo<14 and not final==909 :
    print("NO CONTESTAR")
    
elif final==909:
    print("CONTESTAR")
elif comienzo ==877:
    print("NO CONTESTAR")    

elif tiempo>17 and tiempo<19 and comienzo==877:
    print("CONTESTAR")

else:
    print("NO CONTESTAR")
     