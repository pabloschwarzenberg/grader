nm = input()
nm = list(nm)
contador = 0
unid = len(nm)
for n in nm:
    x = unid-contador
    if x == 4:
        nm[unid-x] = nm[unid-x] +"M"
    if x == 3:
        nm[unid-x] = nm[unid-x] + "C"
    if x == 2:
        nm[unid-x] = nm[unid-x] + "D"
    if x == 1:
        nm[unid-x] = nm[unid-x] + "U"
    contador += 1
auxstr= ""
for n in nm:
    if n.find("U") != -1:
        auxstr += n
    else:
        auxstr += n + "+"
print(auxstr)