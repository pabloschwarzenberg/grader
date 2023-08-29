ing = int(input())
bir = int(input())
chil = int(input())
yea = int(input())
civ = input()
resid = input()

if yea > 10 and chil > 2:
    print("APROBADO")
elif civ == "C" and chil > 3 and 45 < 2021 - yea < 55:
    print("APROBADO")
elif ing > 2500000 and civ == "S" and yea > 5:
    print("APROBADO")
elif resid == "R" and civ == "C" and chil < 2:
    print("APROBADO")
else:
    print("RECHAZADO")