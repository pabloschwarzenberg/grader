#Contestador de celular
NT=input()
H=int(input())
while int(NT)>=100000000 or H<0 or H>23:
    NT=int(input())
if H>=0 and H<=7:
    print("CONTESTAR")
elif H<14 and (int(NT[5:])==909):
    print("CONTESTAR")
elif H<14:
    print("NO CONTESTAR")
elif H>17 and H<19 and (int(NT[0:3])==877):
    print("NO CONTESTAR")
elif H>17 and H<19:
    print("CONTESTAR")
elif H>19:
    print("NO CONTESTAR")