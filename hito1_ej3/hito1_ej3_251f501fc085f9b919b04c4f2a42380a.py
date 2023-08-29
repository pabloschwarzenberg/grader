ingreso = int(input())
adn = int(input())
numhij = int(input())
apb = int(input())
estciv = input()
uor = input()

if apb > 10 and numhij >= 2:
    print("APROBADO")
elif estciv == "C" and numhij > 3 and adn >= 2020 - 45 or adn <= 2020 - 1965:
    print("APROBADO")
elif ingreso > 2500000 and estciv == "S" and uor == "U":
    print("APROBADO")
elif ingreso > 3500000 and apb > 5:
    print("APROBADO")
elif uor == "R" and estciv == "C" and numhij < 2:
    print("APROBADO")
else:
    print("RECHAZADO")

      