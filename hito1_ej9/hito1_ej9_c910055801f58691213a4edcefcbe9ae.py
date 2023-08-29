a = float(input(">>> "))
b = float(input(">>> "))
c = float(input(">>> "))
a2 = float(input(">>> "))
b2 = float(input(">>> "))
c2 = float(input(">>> "))


if a*b2-b*a2 != 0:
    x = (c*b2-b*c2)/(a*b2-b*a2)
    y = (a*c2-c*a2)/(a*b2-b*a2)
else:
    x = None
    y = None


results = ["x="+str(x),"y="+str(y)]
print(results)
