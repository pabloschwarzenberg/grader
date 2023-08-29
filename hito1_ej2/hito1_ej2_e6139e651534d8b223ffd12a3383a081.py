n=int(input("Ingrese numero Telefonico:"))
digitos = [int(x)for x in str(n)]
h=int(input("Ingrese hora de la llamada:"))
if (h==0) or (h==1) or (h==2) or (h==3) or (h==4) or (h==5) or (h==6) or (h==7):
    print ("CONTESTAR")
elif (h==8)or(h==9)or(h==10)or(h==11)or(h==12)or(h==13)or(h==14)and (digitos[5]==9) and (digitos[6]==0) and (digitos[7]==9):
    print ("CONTESTAR")
elif (h==8)or(h==9)or(h==10)or(h==11)or(h==12)or(h==13)or(h==14):
    print ("NO CONTESTAR")
elif (h==17) or(h==18) or(h==19) and (digitos[0]==8)and (digitos[1]==7)and (digitos[2]==7):
    print ("NO CONTESTAR")
elif (h==17) or(h==18) or(h==19):
    print ("CONTESTAR")
elif (h==18) or (h==19)or (h==20)or (h==21)or (h==22)or (h==23):
    print ("NO CONTESTAR")
