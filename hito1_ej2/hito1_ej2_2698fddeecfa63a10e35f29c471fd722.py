#Contestador de celular
N_T=int(input("Ingrese numero de telefono: "))
Hora=int(input("Ingrese hora de llamada: "))
R_C="CONTESTAR"
R_NC="NO CONTESTAR"
if N_T>=10000000 and N_T<=99999999:
  V_aux=(N_T/1000)
  V_aux2=(N_T%1000)
  V_aux3=(N_T//100000)
  if Hora<=7 and Hora>=0: 
    print(R_C)
  if Hora<=14:
    if V_aux2==909:
      print(R_C)
    else:
      print(R_NC)
  if Hora<19 and Hora>=17:
    if V_aux3==877:
      print(R_NC)
    else:
      print(R_C) 
  if Hora>=19:
    print(R_NC)
  if Hora==15 and Hora==16:
    print (R_NC)
