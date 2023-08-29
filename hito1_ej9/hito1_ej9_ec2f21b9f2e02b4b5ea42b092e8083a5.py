l=[int(input(":")),int(input(":")),int(input(":"))]
ll=[int(input(":")),int(input(":")),int(input(":"))]
det=(l[0]*ll[1])-(ll[0]*l[1])
x=(((l[2]*ll[1])-(ll[2]*l[1]))/det).__round__(1)
y=-(((l[2]*ll[0])-(ll[2]*l[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))   