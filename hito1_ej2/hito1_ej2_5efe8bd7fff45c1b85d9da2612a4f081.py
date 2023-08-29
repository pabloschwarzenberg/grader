#Contestador de celular
n = int(input("Su número de celular (8 dgts): \n"))
h = int(input("Hora actual (0 a 23): \n"))
c1 = n - (( n // 10**3) * 10**3)
c2 = (n // 10**5)

if 7 >= h >= 0:
    print("CONTESTAR")

elif 7 < h <= 14 and c1 == 909:
    print("CONTESTAR")
    
elif 17 <= h <= 19 and c2 != 877:
    print("CONTESTAR")

else:
    print("NO CONTESTAR")