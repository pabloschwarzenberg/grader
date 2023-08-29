n = int(input("Ingrese su rut para calcular el digito verificador: "))
n1 = n%10
n2 = int((n%100)/10)
n3 = int((n%1000)/100)
n4 = int((n%10000/1000))
n5 = int((n%100000/10000))
n6 = int((n%1000000/100000))
n7 = int((n%10000000/1000000))
n8 = int((n%100000000/10000000))
n1r = n1*2
n2r = n2*3
n3r = n3*4
n4r = n4*5
n5r = n5*6
n6r = n6*7
n7r = n7*2
n8r = n8*3
s = (n1r+n2r+n3r+n4r+n5r+n6r+n7r+n8r)%11
dv = 11-s
k = "k"
o = 0
if dv == 10:
    print("dv = {}".format(k))
elif dv == 11:
    print("dv = {}".format(o))

else: print("dv = {}".format(dv))