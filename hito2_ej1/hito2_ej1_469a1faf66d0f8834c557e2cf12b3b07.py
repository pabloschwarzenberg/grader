string1 = input()
string2 = input()
lar1 = len(string1)
lar2 = len(string2)
pal1 = []; pal2 = []
pal1 = pal1+ list(string1)
pal2 = pal2+ list(string2)
j = 0;  k = 0;
new = ""
print(lar1, lar2)
while k < len(string1):
    if pal2[j] == pal1[k]:
        new=new+pal1[k]
        j = j + 1
        k = k +1
        z = k
        if z == (lar1):
            while j < lar2:
                new = new + pal2[j]
                j = j+1
    else:
        new=new+"_"
        j = j
        k = k + 1
        z = k
        if z == (lar1):
            while j < lar2:
                new = new + pal2[j]
                j = j+1

print(new)