#Nota final
pt = eval(input("ingrese nota por tareas: "))
pi = eval(input("inserte notas por interogaciones: "))
ne = eval(input("inserte nota po examen: "))
pp = eval(input("inserte notas por presentacion: "))
ptp = pt*0.3 
ptp2 = ptp/100# 0.3
pip = pi*0.3
pip2 = pip/100# 0.3
nep = ne*0.3
nep2 = nep/100# 0.3
ppp = pp*0.1
ppp2 = ppp/100# 0.3
pf = ptp+pip+nep+ppp
pff = pf/4
pf = round(pf,1)
print("el promedio es:",pf)