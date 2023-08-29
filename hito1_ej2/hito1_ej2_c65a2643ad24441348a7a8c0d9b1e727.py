#Contestador de celular
num=input('ingresa numero')
hor=int(input('hora de llamada'))
if len(num)==8:
    if hor>=0 and hor <=7:
        print('contestar')
    elif hor ==14 or hor==13 or hor==12 or hor==11 or hor ==10 or hor ==9 or hor==8 and num[-1]==9 and num[-2]==0 and num[-3]==9:
       print("CONTESTAR")
    elif hor==17 or hor==19 or hor==18:
       print('no contestar')
    elif hor==17 or hor==19 or hor==18 and num[0]==8 and num[1]==7 and num[2]==7:
        print('contestar')
    elif hor>19:
       print('no contestar')
    