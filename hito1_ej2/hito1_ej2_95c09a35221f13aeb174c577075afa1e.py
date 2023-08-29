n=int(input(":"))
h=int(input(":"))
a=int(n % 1000)
b=(round(n/100000),0)

if 0 < h < 7:
    print("CONTESTAR")

elif 7 < h < 14 and (a == 909):
    print("CONTESTAR")

elif 7 < h < 14 and (a != 909):
    print("NO CONTESTAR")

elif 17 <= h <= 19 and b == 887.0:
    print("CONTESTAR")

elif 17 <= h <= 19 and b != 887.0:
    print("NO CONTESTAR")

elif h >= 19:
    print("NO CONTESTAR")

else:
    print("NO CONTESTAR")
