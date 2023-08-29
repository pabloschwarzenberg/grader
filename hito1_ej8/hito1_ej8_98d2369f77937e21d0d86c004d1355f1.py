n = int(input("ingrese numero:"))

mil = n / 1000
p = n % 1000

cen = p / 100
p = p % 100

dec = p / 10
u = p % 10

print("%i" % mil,"M+", "%i" % cen, "C+", "%i" % dec,"D+", "%i" % u, "U" )