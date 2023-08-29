a = str(input())

if int(a) < 10:
    print("{}U".format(a))
elif 10 <= int(a) < 100:
    print("{}D + {}U".format(a[0], a[1]))
elif 100 <= int(a) < 1000:
    print("{}C + {}D + {}U".format(a[0], a[1], a[2]))
elif int(a) >= 1000:
    print("{}M + {}C + {}D + {}U".format(a[0], a[1], a[2], a[3]))


      