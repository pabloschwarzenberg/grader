#Cálculo del dígito verificador de un rut
rut=str(input())
d1=int(rut[0:1])
d2=int(rut[1:2])
d3=int(rut[2:3])
d4=int(rut[3:4])
d5=int(rut[4:5])
d6=int(rut[5:6])
d7=int(rut[6:7])
if len(rut) == 8:
   d8=int(rut[7:])
   nd8=d8*2
   nd7=d7*3
   nd6=d6*4
   nd5=d5*5
   nd4=d4*6
   nd3=d3*7
   nd2=d2*2
   nd1=d1*3
   ndx=nd1+nd2+nd3+nd4+nd5+nd6+nd7+nd8
   ndy=((ndx)%11)
   if ndy == 0:
      print ("dv=0")
   else:
      dvx=(11-ndy)
      if dvx == 10:
         print ("dv=k")
      else:
         dvy=str(dvx)
         print ("dv="+dvy)
else:
    nd7=d7*2
    nd6=d6*3
    nd5=d5*4
    nd4=d4*5
    nd3=d3*6
    nd2=d2*7
    nd1=d1*2
    ndx=nd1+nd2+nd3+nd4+nd5+nd6+nd7
    ndy=((ndx)%11)
    if ndy == 0:
       print ("dv=0")
    else:
       dvx=(11-ndy)
       if dvx == 10:
          print ("dv=k")
       else:
          dvy=str(dvx)
          print ("dv="+dvy)