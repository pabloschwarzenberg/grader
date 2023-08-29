x = str(input())
d =""
if len(x) == 4:
    d = str(x[0])+"M + "+ str(x[1])+"C + "+ str(x[2])+"D + "+ str(x[3])+"U"
if len(x) == 3:
    d = str(x[0])+"C + "+ str(x[1])+"D + "+ str(x[2])+"U"
if len(x) == 2:
    d = str(x[0])+"D +"+ str(x[1])+"U"
if len(x)==1:
    d = str(x[1])+"U"

print(d)
    