#Contestador de celular
num= int(input())
hor= int(input())
if 0<hor<7:
    print("CONTESTAR")
if 7<hor<14 and num-((num//1000)*1000)==909:
    print("CONTESTAR")
elif 17<hor<19 and num//100000!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")