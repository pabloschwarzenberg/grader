NU=int(input("Ingrese numero telefonico: "))
H=int(input("Ingrese hora de la llamada: "))
NUX=str(NU)[5:8]
NUX1=str(NU)[:3]
NUX=int(NUX)
NUX1=int(NUX1)

CON=0
NOCON=0
if H<7 and H>0:
    CON=1
if H<14 and H>7:
    NOCON=1
    if NUX==909:
        CON=1
        NOCON=0
if H>15 and H<24:
    NOCON=1
    if H>17 and H<19:
        CON=1
        NOCON=0
        if H>17 and H<19 and NUX1==877:
            NOCON=1
            CON=0
if CON<NOCON:
    print ("NO CONTESTAR")
else:
    print ("CONTESTAR")
