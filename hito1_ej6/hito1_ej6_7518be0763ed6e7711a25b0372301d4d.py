N1 = int(input("ingresa un numero: "))
N2 = int(input("ingresa un segundo numero: "))
N3 = int(input("ingresa un tercer numero: "))
if N1 <= N2 <= N3:
    print("{N1} {N2} {N3}")
elif N1 <= N3 <= N2:
    print("{N1} {N3} {N2}")
elif N2 <= N1 <= N3:
    print("{N2} {N1} {N3}")
elif N2 <= N3 <= N1:
    print("{N2} {N3} {N1}")
elif N3 <= N2 <= N1:
    print("{N3} {N2} {N1}")
else:
    print("{N3} {N1} {N2}")