
v1 = int(input("ingrese valor uno: "))
v2 = int(input("ingrese valor dos : "))
v3 = int(input("ingrese valor tres : "))

if v1 <= v2 <= v3:
    print("%d, %d, %d" % (v1, v2, v3))
if v1 <= v3 <= v2:
    print("%d, %d, %d" % (v1, v3, v2))
if v2 <= v1 <= v3:
    print("%d, %d, %d" % (v2, v1, v3))
if v2 <= v3 <= v1:
    print("%d, %d, %d" % (v2, v3, v1))
if v3 <= v1 <= v2:
    print("%d, %d, %d" % (v3, v1, v2))
if v3 <= v2 <= v1:
    print("%d, %d, %d" % (v3, v2, v1))

