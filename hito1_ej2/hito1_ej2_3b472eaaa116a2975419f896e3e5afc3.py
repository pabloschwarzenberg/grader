#Contestador de celular
n=int(input())
h=int(input())
if 0<=h<=7:
    print("CONTESTAR")
elif h<=14:
    if n%1000==909 :
        print("CONTESTAR")
    else:        
        print("NO CONTESTAR")
elif 17<=h<=19:
    if n//(10**5)==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif h>19:
    print("NO CONTESTAR")
        
         