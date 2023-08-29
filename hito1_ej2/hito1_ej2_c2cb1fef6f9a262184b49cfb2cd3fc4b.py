num = input()
hor = int(input())
udig = num[-3:]
pdig = num[:3]
if hor <= 7:
    print("CONTESTAR")
elif hor > 7 and hor < 14 and udig == "909":
    print("CONTESTAR")
elif hor >= 17 and hor <= 19 and pdig != "877":
    print("CONTESTAR")
else:
    print("NO CONTESTAR")