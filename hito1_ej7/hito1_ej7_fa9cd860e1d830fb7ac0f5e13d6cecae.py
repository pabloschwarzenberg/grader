x = int(input("Ingresa dia: "))
y = int(input("Ingresa mes: "))

if y == 1:
    if 0 <= x < 20:
        print("Capricorn")
    if 20 <= x <= 31:
        print("Aquarius")
if y == 2:
    if 0 <= x < 19:
        print("Aquarius")
    if 19 <= x < 31:
        print("Pisces")
if y == 3:
    if 0 <= x < 21:
        print("Pisces")
    if 21 <= x < 31:
        print("Aries")
if y == 4:
    if 0 <= x < 21:
        print("Aries")
    if 21 <= x < 31:
        print("Taurus")
if y == 5:
    if 0 <= x < 21:
        print("Taurus")
    if 0 <= x < 31:
        print("Gemini")
if y == 6:
    if 0 <= x < 21:
        print("Gemini")
    if 21 <= x < 31:
        print("Cancer")
if y == 7:
    if 0 <= x < 23:
        print("Cancer")
    if 23 <= x < 31:
        print("Leo")
if y == 8:
    if 0 <= x < 23:
        print("Leo")
    if 23 <= x < 31:
        print("Virgo")
if y == 9:
    if 0 <= x < 23:
        print("Virgo")
    if 23 <= x < 31:
        print("Libra")
if y == 10:
    if 0 <= x < 23:
        print("Libra")
    if 23 <= x < 31:
        print("Scorpio")
if y == 11:
    if 0 <= x < 23:
        print("Scorpio")
    if 23 <= x < 31:
        print("Sagittarius")
if y == 12:
    if 0 <= x < 22:
        print("Sagittarius")
    if 22 <= x < 31:
        print("Capricorn")