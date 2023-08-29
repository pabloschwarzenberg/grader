sal_caj= 1000000
us=10334151
cl = 1803
sal_cnt = 100000
mon_ret=0
ing_us=0
cl_ing =0
intento= 0
billetes_de_20 =20
billetes_de_10 =40
billetes_de_5 =40
while True:
    ing_us=int(input())
    cl_ing = int(input())
    
    if cl != cl_ing:
        print("clave invalida")
        intento + 1
    if intento>3:
        break
    if cl==cl_ing:
        mon_ret=int(input())
        if mon_ret>sal_cnt:
            print("monto no permitido")
        if mon_ret<=sal_cnt:
            break
        
if mon_ret<sal_cnt:
    sal_f_cnt= sal_cnt - mon_ret
    sal_f_caj = sal_caj - mon_ret
    print("saldo cuenta=",sal_f_cnt)
    print("saldo cajero=",sal_f_caj)
if mon_ret>=20000:
    division = mon_ret//20000
    billetes_de_20 = division
    resto = mon_ret%20000
    division2 = resto//10000
    billetes_de_10 = division2
    resto2 = resto%10000
    division3 = resto2//5000
    billetes_de_5 = division3
if mon_ret<20000 and mon_ret>=10000:
    division = mon_ret//10000
    billetes_de_10 = division
    resto = mon_ret % 10000
    division2 = resto//5000
    billetes_de_5 = division2
    billetes_de_20 = 0
if mon_ret<10000 and mon_ret>=5000:
    division = mon_ret//5000
    billetes_de_5 = division
    billetes_de_20 = 0
    billetes_de_10 = 0

print("billetes 20000=",billetes_de_20)
print("billetes 10000=",billetes_de_10)
print("billetes 5000=",billetes_de_5)

    
if intento>3:
    print("tarjeta bloqueada")