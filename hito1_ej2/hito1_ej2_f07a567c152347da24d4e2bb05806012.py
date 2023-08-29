num = int(input())
hrs = int(input())


a = (num//10000000)%10
b = (num//1000000)%10
c = (num//100000)%10
cen = (num//100)%10
dec = (num//10)%10
uni = num%10

if 00<=hrs<7:
    print("CONTESTAR")

if 7<=hrs<14:
    if cen==9 and dec==0 and uni==9:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

if 17<=hrs<19:
    if a==8 and b==7 and c==7:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if 17<=hrs<19:
    if a==8 and b==7 and c==7:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

if 14<=hrs<17:
    print("NO CONTESTAR")
if 19<=hrs<24:
    print("NO CONTESTAR")
      