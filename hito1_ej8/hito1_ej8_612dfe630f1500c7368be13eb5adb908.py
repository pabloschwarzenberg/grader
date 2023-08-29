num=int(input("Indique número: "))

if len(str(num)) == 1:
    u=str(num)[0]
    print(f"{u}U")
if len(str(num)) == 2:
    d=num//10
    u=num%10
    print(f"{d}D + {u}U")
if len(str(num)) == 3:
    u = str(num)[2]
    d=str(num)[1]
    c=str(num)[0]
    print(f"{c}C + {d}D + {u}U")
if len(str(num)) == 4:
    u = str(num)[3]
    d = str(num)[2]
    c = str(num)[1]
    um = str(num)[0]
    print(f"{um}M + {c}C + {d}D + {u}U")