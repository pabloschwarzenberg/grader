tel = input("num: ")
hora = int(input("hora: "))

if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora < 14:
    if tel[5:8] == '909':
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if tel[0:3] == '877':
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
