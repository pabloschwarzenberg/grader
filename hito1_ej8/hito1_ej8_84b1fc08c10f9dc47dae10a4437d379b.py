def uni():
    uni = str(lis[0])+"U"
    return uni
def dece():
    dece = str(lis[1])+"D"
    return dece
def cent():
    cent = str(lis[2])+"C"
    return cent
def mil():
    mil = str(lis[3])+"M"
    return mil
    
n = int(input("Numero: "))

lis = []

while n >= 1:
    aux = n%10
    lis.append(aux)
    n = n//10
if len(lis) == 4:
    print(mil()+" + "+cent()+" + "+dece()+" + "+uni())
elif len(lis) == 3:
    print(cent()+" + "+dece()+" + "+uni())
elif len(lis) == 2:
    print(dece()+" + "+uni())
else:
    print(uni())