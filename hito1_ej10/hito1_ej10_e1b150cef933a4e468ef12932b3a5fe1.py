sal_caj = 1000000
us =10334151
cl = 1803
sal_cnt = 100000
mon_ret = 0
ing_us = 0
cl_ing = 0
intento = 0
while True:
    ing_us = int(input("ingrese usuario:"))
    cl_ing = int(input("ingrese su clave:"))
    if cl != cl_ing:
        print("clave invalida")
        intento + 1
    if intento>3:
        break
    if cl==cl_ing:
        mon_ret=int(input("ingrese monto a retirar:"))
        if mon_ret>sal_cnt:
            print("monto no permitido")
        if mon_ret<sal_cnt:
            break
        
if mon_ret<sal_cnt:
    s_f_ct = sal_cnt - mon_ret
    s_f_cj = sal_caj - mon_ret
    print("saldo cuenta=",s_f_ct)
    print("saldo cajero=",s_f_cj)
    
if intento>3:
    print("tarjeta bloqueada")