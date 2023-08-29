a=int(input())
b=int(input())
a=str(a)
q=len(a)
o1=q-1
o2=q-2
o3=q-3
if int(a[o1])==9:
    if int(a[o2])==0:
        if int(a[o3])==9:
            if b<14:
                if b>7:
                    print("CONTESTAR")
if b>=0:
    if b<=7:
        print("CONTESTAR")
if b>=17:
    if b<=19:
        if int(a[0])==8:
            if int(a[1])==7:
                if int(a[2])==7:
                    print("NO CONTESTAR")
if b>19:
    if b<=23:
        print("NO CONTESTAR")
if b>=17:
    if b<=19:
        if int(a[0])!=8:
            if int(a[1])!=7:
              if int(a[2])!=7:
                print("CONTESTAR")
         
             
if b<14:
    if b>7:
        if int(a[o1])!=9:
            print("NO CONTESTAR")