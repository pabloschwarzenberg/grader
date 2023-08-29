d = int(input(" "))
m = int(input(" "))

if 4 >= m >= 3 and 18 >= d >= 1:
    print("Aries")
elif 4 >= m >= 3 and 31 >= d >= 20:
    print("Aries")
elif 5 >= m >= 4 and 31 >= d >= 21:
    print("Taurus")
elif 5 >= m >= 4 and 21 >= d >= 1:
    print("Taurus")
elif 6 >= m >= 5 and 31 >= d >= 22:
    print("Gemini")
elif 6 >= m >= 5 and 21 >= d >= 1:
    print("Gemini")
elif 7 >= m >= 6 and 31 >= d >= 22:
    print("Cancer")
elif 7 >= m >= 6 and 22 >= d >= 1:
    print("Cancer")
elif 8 >= m >= 7 and 31 >= d >= 23:
    print("Leo")
elif 8 >= m >= 7 and 22 >= d >= 1:
    print("Leo")
elif 9 >= m >= 8 and 31 >= d >= 23:
    print("Virgo")
elif 9 >= m >= 8 and 23 >= d >= 1:
    print("Virgo")
elif 10 >= m >= 9 and 31 >= d >= 24:
    print("Libra")
elif 10 >= m >= 9 and 24 >= d >= 1:
    print("Libra")
elif 11 >= m >= 10 and 31 >= d >= 24:
    print("Scorpio")
elif 11 >= m >= 10 and 22 >= d >= 1:
    print("Scorpio")
elif 12 >= m >= 11 and 31 >= d >= 23:
    print("Sagittarius")
elif 12 >= m >= 11 and 21 >= d >= 1:
    print("Sagittarius")
elif 1 == m or m == 12 and 31 >= d >= 22:
    print("Capricorn")
elif 1 == m or m == 12 and 20 >= d >= 1:
    print("Capricorn")
elif 2 >= m >= 1 and 31 >= d >= 21:
    print("Aquarius")
elif 2 >= m >= 1 and 19 >= d >= 1:
    print("Aquarius")
elif 3 >= m >= 2 and 28 >= d >= 20:
    print("Pisces")
elif 3 >= m >= 2 and 20 >= d >= 1:
    print("Pisces")
else:
    print("Error de escritura")