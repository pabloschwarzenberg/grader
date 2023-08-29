#Contestador de celular
x=str(input())
h=int(input())

if 0<=h<=7 :
    print("CONTESTAR")
elif h<14 and x[5]!=9 and x[6]!=0 and x[7]!=9 :
    print("CONTESTAR")
elif 17<=h<=19 and x[0]!=8 and x[1]!=7 and x[2]!=7 :
    print("NO CONTESTAR")
else :
    print("NO CONTESTAR")