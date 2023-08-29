rut = input ()
19858367
a = rut[:1]
b = rut[:2][1:]
c = rut[:3][2:]
d = rut[:4][3:]
e = rut[:5][4:]
f = rut[:6][5:]
g = rut[:7][6:]
if len(rut) == 7:
                suma = int(a) * 2 + int(b) * 7 + int(c) * 6 + int(d) * 5 + int(e) * 4 + int(f) * 3 + int(g) * 2
                resto = int(suma) % 11
                resultado = 11 - int(resto)
                if (int(resultado) == 10): print ("dv=" + "k")
                elif (int(resultado) == 11): print ("dv=" + "0")
                else: print ("dv=", resultado)
elif len(rut) == 8:
                h = rut[7:]
                suma = (int(a) * 3) + (int(b) * 2) + (int(c) * 7) + (int(d) * 6) + (int(e) * 5) + (int(f) * 4) + (int(g) * 3) + (int(h) * 2)
                resto = int(suma) % 11
                resultado = 11 - int(resto)
                if (int(resultado) == 10): print ("dv=" + "k")
                elif (int(resultado) == 11): print ("dv=" + "0")
                else: print ("dv=", resultado)




