#Contestador Automático
n= int(input())
h= int(input())
if 0<=h<=7:
    print("CONTESTAR")
if 7<h<14:
    if n%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 14<=h<17:
    print("NO CONTESTAR")
if 17<=h<=19:
    if n//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if h>19:
    print("NO CONTESTAR")