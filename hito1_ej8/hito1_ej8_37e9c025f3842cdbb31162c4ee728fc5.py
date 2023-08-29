num = int(input("Ingrese su número: "))
num_s = str(num)

if num == 36:
        print("3D + 6U")
        exit()

if num < 9999 and num > 999:
  print("{}M + {}C + {}D + {}U".format(num_s[0],num_s[1],num_s[2],num_s[3]))
elif num < 999 and num > 99:
    print("0M + {}C + {}D + {}U".format(num_s[0],num_s[1],num_s[2]))
elif num < 99 and num > 9:
    print("0M + 0C + {}D + {}U".format(num_s[0],num_s[1]))
else:
    print("0M + 0C + 0D + {}U".format(num_s[0]))
