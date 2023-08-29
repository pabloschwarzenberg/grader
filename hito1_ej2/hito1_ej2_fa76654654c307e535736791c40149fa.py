num=int(input())
hr=int(input())
numa=num%1000
numb=num//100000

if 0<=hr<=7:
    print("CONTESTAR")

if 7<hr<=14:
    if numa==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if 17<=hr<=19:
    if numb==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
            
if hr>=19:
    print("NO CONTESTAR")
