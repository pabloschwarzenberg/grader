Rut= (input("Introducir rut sin puntos ni digito verificador: ")[::-1])
len(Rut)==8
d1= int(Rut[0])*2
d2= int(Rut[1])*3
d3= int(Rut[2])*4
d4= int(Rut[3])*5
d5= int(Rut[4])*6
d6= int(Rut[5])*7
d7= int(Rut[6])*2
d8= int(Rut[7])*3
ResultadoSuma= (d1+d2+d3+d4+d5+d6+d7+d8)
ResultadoObtenidoSuma= ((ResultadoSuma)//11)
ResultadoObtenidoDivision= (ResultadoObtenidoSuma*11)
ResultadoFinalp_1= abs(ResultadoSuma-ResultadoObtenidoDivision)
ResultadoFinalp_2= (11-(ResultadoFinalp_1))
if (ResultadoFinalp_2)== 11:
    print ("dv=0")
if (ResultadoFinalp_2)== 10:
    print ('dv=k')
else:
    print ('dv='+str(ResultadoFinalp_2))
