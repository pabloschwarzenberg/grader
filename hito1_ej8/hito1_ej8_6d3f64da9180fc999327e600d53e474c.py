print ("Introduce el número: ")
numero = int(input ())

mil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10

print ("Mil: %iM " % mil)
print ("Centenas: %iC" % centenas)
print ("Decenas: %iD" % decenas)
print ("Unidades: %iU" % unidades)
m = "%iM" % mil
c = "%iC" % centenas
d = "%iD" % decenas
u = "%iU" % unidades
print (m ,"+" ,c ,"+" ,d ,"+" ,u )