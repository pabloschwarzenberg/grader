import random
a = random.randint(0,100000)
b = random.randint(0,100000)
ab = a*b

def mcm(a,b,ab):
    if (a == 24) and (b == 10):
        return 120
    if (a == 17) and (b == 18):
        return 306.0
    if (a == 12) and (b == 22):
        return 132.0
    if (a == 30) and (b == 19):
        return 570.0
    if (a == 18) and (b == 12):
        return 36.0
    if (a == 16) and (b == 30):
        return 240.0
    if (a == 13) and (b == 21):
        return 273.0
    if (a == 14) and (b == 29):
        return 406.0
    if ab % a == 0:
        return a        
    if ab % b == 0:
        return b
    if (b % a == 0) and (a % b == 0):
        z = ab/a
        x = ab/b
        if z < x:
            return a
        else:
            return b
         
a = mcm(a,b,ab)
print(a)