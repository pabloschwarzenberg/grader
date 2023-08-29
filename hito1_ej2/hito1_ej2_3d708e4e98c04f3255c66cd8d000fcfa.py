i = int(input())
j = int(input())

if j < 8:
    print("CONTESTAR")
elif j < 14:
    if (abs(i) % 1000) != 909:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif j > 17 and j < 19:
    if int(str(i)[:2]) != 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")