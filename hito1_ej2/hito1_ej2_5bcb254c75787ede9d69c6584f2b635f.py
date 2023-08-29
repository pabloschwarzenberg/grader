#Contestador de celular
n=int(input())  
h=int(input())
if (0<=h>=7):
    print ("contestar")
if (7<h<14):
    if (n%1000==909):
        print("contestar")
    else:
        print("contestar")
if (14<=h<15):
    print ("no contestar")
if (15<=h<=19):
    if (n//1000==877):
        print("contestar")
    else:
        print("no contestar")
if (h>19):
    print ("no contestar")

