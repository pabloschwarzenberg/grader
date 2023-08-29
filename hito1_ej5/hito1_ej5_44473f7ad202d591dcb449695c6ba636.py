#Cálculo del dígito verificador de un rut
n = input("Ingrese rut sin digito verificador:")
if len(n) == 8:
    sep = (int(n[7])) * 2
    sext = (int(n[6])) * 3
    quin = (int(n[5])) * 4
    cuar = (int(n[4])) * 5
    tercer = (int(n[3])) * 6
    segun = (int(n[2])) * 7
    primero = (int(n[1])) * 2
    cero = (int(n[0])) * 3
    todos = sep + sext + quin + cuar + tercer + segun + primero + cero
    parteent = todos // 11
    rest = todos - (11 * parteent)
    a = 11 - rest
    if a == 11:
        a = 0
    if a == 10:
        a = str("k")
if len(n) == 7:
    sext = (int(n[6])) * 2
    quin = (int(n[5])) * 3
    cuar = (int(n[4])) * 4
    tercer = (int(n[3])) * 5
    segun = (int(n[2])) * 6
    primero = (int(n[1])) * 7
    cero = (int(n[0])) * 2
    todos = sext + quin + cuar + tercer + segun + primero + cero
    parteent = todos//11
    rest = todos - (11*parteent)
    a = 11 - rest
    if a == 11:
        a = 0
    if a == 10:
        a = str("k")
print("dv=",a)     