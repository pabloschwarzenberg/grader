n=int(input())
h=int(input())
if (0<h<7):
    print("CONTESTAR")
if (7<h<14) and ((n%100000)!=909):
    print("CONTESTAR")
if (7<h<14) and ((n%100000)==909):
    print("NO CONTESTAR")
if (17<h<19) and ((n//1000000)!=877):
    print("NO CONTESTAR")
if (17<h<19) and ((n//1000000)==877):
    print("CONTESTAR")
if (14<h<17):
    print("NO CONTESTAR")
if (19<h<24):
    print("NO CONTESTAR")
