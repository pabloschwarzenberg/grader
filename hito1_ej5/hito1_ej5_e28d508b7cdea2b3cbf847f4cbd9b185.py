R = str(input())

if len(R) == 8 :
    x =((int(R[0]) * 3) + (int(R[1]) * 2) + (int(R[2]) * 7) + (int(R[3]) * 6) + (int(R[4]) * 5) + (int(R[5]) * 4) + (int(R[6]) * 3) + (int(R[7]) * 2))
if len(R) == 7:
    x = ((int(R[0]) * 2) + (int(R[1]) * 7) + (int(R[2]) * 6) + (int(R[3]) * 5) + (int(R[4]) * 4) + (int(R[5]) * 3) + (int(R[6]) * 2))
if len(R) == 6:
    x = ((int(R[0]) * 7) + (int(R[1]) * 6) + (int(R[2]) * 5) + (int(R[3]) * 4) + (int(R[4]) * 3) + (int(R[5]) * 2))
if len(R) == 5:
    x = ((int(R[0]) * 6) + (int(R[1]) * 5) + (int(R[2]) * 4) + (int(R[3]) * 3) + (int(R[4]) * 2))
if len(R) == 4:
    x = ((int(R[0]) * 5) + (int(R[1]) * 4) + (int(R[2]) * 3) + (int(R[3]) * 2))
if len(R) == 3:
    x = ((int(R[0]) * 4) + (int(R[1]) * 3) + (int(R[2]) * 2))
if len(R) == 2:
    x = ((int(R[0]) * 3) + (int(R[1]) * 2))
if len(R) == 1:
    x = ((int(R[0]) * 2))

U = int(x) % 11
D = 11 - U
if D == 10:
    print("dv=k")
elif  D==11:
    print("dv=0")
else:
    print("dv=", D)