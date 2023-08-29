pt = eval(input("ingrese puntos de tarea: "))
pi = eval(input("ingrese puntos de interrogciones: "))
ne = eval(input("ingrese nota de examen: "))
pp = eval(input("ingrese nota de precentacion: "))


ptt = pt * 0.3
pii = pi * 0.3
nee = ne * 0.3
ppp = pp * 0.1
ntf = ptt + pii + nee + ppp
print("su nota es: ",round(ntf,1))