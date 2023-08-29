#Contestador de celular
cel=int(input())
time=int(input())
if 0<=time<=7:
    print("CONTESTAR")
elif cel%1000==909 and 14>time>7: 
    print("CONTESTAR")
elif cel%1000!=909 and 14>time>7:  
    print("NO CONTESTAR")
elif cel//100000==877 and 14<=time<=19:
    print("NO CONTESTAR")
elif cel//100000!=877 and 14<=time<=19:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")