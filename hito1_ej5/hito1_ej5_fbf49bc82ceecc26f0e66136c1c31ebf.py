print("Ingrese su rut:")
rut = str(input())
largo = len(rut)
if(largo == 8):
   rut1 = int(rut[7]) * 2
   rut2 = int(rut[6]) * 3
   rut3 = int(rut[5]) * 4
   rut4 = int(rut[4]) * 5
   rut5 = int(rut[3]) * 6
   rut6 = int(rut[2]) * 7
   rut7 = int(rut[1]) * 2
   rut8 = int(rut[0]) * 3
   rut9 = rut1 + rut2 + rut3 + rut4 + rut5 + rut6 + rut7 + rut8
   rut10 = rut9 // 11
   rut11 = rut9 - (11 * rut10)
   rut12 = 11 - rut11
   if (rut12 == 11):
       print(0)
   elif (rut12 == 10):
       print("dv=k")
   else:
       print(rut12)
elif(largo == 7):
    rut2 = int(rut[6]) * 2
    rut3 = int(rut[5]) * 3
    rut4 = int(rut[4]) * 4
    rut5 = int(rut[3]) * 5
    rut6 = int(rut[2]) * 6
    rut7 = int(rut[1]) * 7
    rut8 = int(rut[0]) * 2
    rut9 = rut2 + rut3 + rut4 + rut5 + rut6 + rut7 + rut8
    rut10 = rut9 // 11
    rut11 = rut9 - (11 * rut10)
    rut12 = 11 - rut11
    if (rut12 == 11):
        print("dv=",0)
    elif (rut12 == 10):
        print("dv=k")
    else:
        print("dv=",rut12)   