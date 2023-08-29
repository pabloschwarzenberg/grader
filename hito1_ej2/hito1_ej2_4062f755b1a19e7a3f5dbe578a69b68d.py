#Contestador de celular
numero = input ()
77389909
hora = input ()
13
if (0 <= int(hora) <= 7): print ("CONTESTAR")
elif ((7 < int(hora) <= 14) and (((numero[5:]) == "909"))): print ("CONTESTAR")
elif ((7 < int(hora) <= 14) and (((numero[5:]) != "909"))): print ("NO CONTESTAR")
elif (14 < int(hora) <= 17): print ("NO CONTESTAR")
elif (((17 < int(hora) <= 19) and ((numero[:3] != "877")))): print ("CONTESTAR")
elif (((17 < int(hora) <= 19) and ((numero[:3] == "877")))): print ("NO CONTESTAR")
else: print ("NO CONTESTAR")      