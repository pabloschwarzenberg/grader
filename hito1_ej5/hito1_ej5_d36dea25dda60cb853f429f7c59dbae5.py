rut = input("Rut: ")
dv = 0
n_mult = 2
for digito in reversed(rut):
    
    digito = int(digito)
    mult = digito*n_mult
    n_mult += 1
    dv += mult
    if n_mult == 8:
        n_mult = 2
    
dv =  dv%11
dv = 11 - dv
dv = str(dv)
if dv == "10":
    print("dv=k")
if dv == "11":
 print("dv=0")

else: print("dv="+dv)
