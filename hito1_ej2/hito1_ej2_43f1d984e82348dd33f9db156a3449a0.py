num=input()
hora=int(input())
if 0<hora<7:
    print("CONTESTAR")
elif str(num)[5:8]=="909" and hora<19:
    print("CONTESTAR")
elif 7<hora<14:
    print("NO CONTESTAR")
elif 17<hora<19 and str(num)[0:3]!="877":
    print("CONTESTAR")
elif 17<hora<19 and str(num)[0:3]=="877":
    print("NO CONTESTAR")
elif 19<hora:
    print("NO CONTESTAR")
