l=[]
c=0
for x in range(4):
    if x<3:
        n=float(input(":"))*0.3
        c+=n
    else:
        n = float(input(":")) * 0.1
print(c.__round__(1))