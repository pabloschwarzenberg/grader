#Contestador de celular
nro=int(input("Ingrese el número de teléfono:"))
hora=int(input("Ingrese la hora:"))

nce=nro//10000000
nu=((nro-nce*10000000)//1000000)
nd=((nro-(nce*10000000+nu*1000000))//100000)
nt=((nro-(nce*10000000+nu*1000000+nd*100000))//10000)
ncu=((nro-(nce*10000000+nu*1000000+nd*100000+nt*10000))//1000)
nc=((nro-(nce*10000000+nu*1000000+nd*100000+nt*10000+ncu*1000))//100)
nse=((nro-(nce*10000000+nu*1000000+nd*100000+nt*10000+ncu*1000+nc*100))//10)
ns=((nro-(nce*10000000+nu*1000000+nd*100000+nt*10000+ncu*1000+nc*100+nse*10)))

if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora<14:
   if nc==9 and nse==0 and ns==9:
       print("CONTESTAR")
   else:
       print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if nce==8 and nu==7 and nd==7:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")