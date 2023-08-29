cadena = input()
num = int(input())
subs = []
i = 0

while i+num < len(cadena)+1:
    subt = cadena[i:i+num].lower()
    subs.append(subt)
    i += 1
j = 0
shadow =[]
while j < len(subs):
    subused = subs[j+1:]
    rep = 0
    for items in subused:
        if subs[j] == items:
            next = subused.index(subs[j])
            subs.pop(next+j+1)
            rep += 1
            continue
    if rep > 0:
        shadow.insert(0,j)
    j += 1

if len(shadow) > 0:
    for banned in shadow:
        subs.pop(banned)
if len(subs) > 0:
    for yay in subs:
        print(yay)
else:
    print(["ninguna"])
