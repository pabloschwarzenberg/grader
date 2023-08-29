#Zodiaco
dia = int(input("Ingrese dia "))
mes = int(input("Ingrese mes "))
scal = str(mes).rjust(2, '0')+str(dia).rjust(2, '0')
signo = ""

if scal > "0321" and scal <= "0420" : signo = "aries"
elif scal > "0420" and scal <= "0521" : signo = "tauro"
elif scal > "0521" and scal <= "0621" : signo = "geminis"
elif scal > "0621" and scal <= "0723" : signo = "cancer"
elif scal > "0723" and scal <= "0823" : signo = "leo"
elif scal > "0823" and scal <= "0923" : signo = "virgo"
elif scal > "0923" and scal <= "1023" : signo = "libra"
elif scal > "1023" and scal <= "1122" : signo = "escorpion"
elif scal > "1122" and scal <= "1222" : signo = "sagitario"
elif (scal > "1222" and scal <= "1231") or (scal >= "0101" and scal <= "0120")  : signo = "capricornio"
elif scal > "0120" and scal <= "0219" : signo = "acuario"
elif scal > "0219" and scal <= "0321" : signo = "piscis"

print(signo)