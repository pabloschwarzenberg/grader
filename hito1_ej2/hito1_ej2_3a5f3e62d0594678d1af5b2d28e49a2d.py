A=int(input())
h=int(input())
if len(str(A))==8:
    if h>=0 and h<7:
        print("CONTESTAR")
    elif h>=7 and h<=14:
        if A%1000==909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")        
    if h>14 and h<=19:
        if A//100000==877:
            print("NO CONTESTAR")
        else:
            print("CONTESTAR") 
    if h>19 and h<24:
        print("NO CONTESTAR")
