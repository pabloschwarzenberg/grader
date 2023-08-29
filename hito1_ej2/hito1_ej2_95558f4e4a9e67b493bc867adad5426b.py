t = int(input('telefono: '))
h = int(input('hora: '))
nt = str(t)
u = int(nt[-3:])
p = int(nt[:3])
if h >= 0 and h <= 7:
    print('CONTESTAR')
elif h > 7 and h < 14:
    if u == 909:
        print('CONTESTAR')
    else:
        print('NO  CONTESTAR')
elif h >= 14 and h < 17:
    print('NO CONTESTAR')
elif h >= 17 and h <= 19:
    if p == 877:
        print('NO CONTESTAR')
    else:
        print('CONTESTAR')
elif h > 19:
    print('NO CONTESTAR')
      