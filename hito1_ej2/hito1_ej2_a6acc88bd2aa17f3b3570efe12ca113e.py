tel=input(":")
hora=int(input(":"))
if hora>=0 and hora<=7:
    print("CONTESTAR")
elif tel[5:]=="909":
    print("CONTESTAR")
elif tel[:3]!="877" and (hora>=17 and hora<=19):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")