c=0
toto=0
totot=0
a =list(input("ingrese rut"))
if len(a)==8:
      o1 = int(a[7]) * 2
      o2 = int(a[6]) * 3
      o3 = int(a[5]) * 4
      o4 = int(a[4]) * 5
      o5 = int(a[3]) * 6
      o6 = int(a[2]) * 7
      o7 = int(a[1]) * 2
      o8 = int(a[0]) * 3
      sumo=(o1+o2+o3+o4+o5+o6+o7+o8)
      divo=int(sumo/11)
      toto=sumo-(11*divo)
      totot = 11 - toto
      tol = str(totot)
      if totot==10:
          tol="k"
      print("dv=" + tol)
      if totot==10:
          tol="0"
      print("dv=" + tol)
elif len(a)==7:
     print(a[3])
     o1 = int(a[6]) * 2
     o2 = int(a[5]) * 3
     o3 = int(a[4]) * 4
     o4 = int(a[3]) * 5
     o5 = int(a[2]) * 6
     o6 = int(a[1]) * 7
     o7 = int(a[0]) * 2
     sumo = (o1 + o2 + o3 + o4 + o5 + o6 + o7 )
     divo = int(sumo / 11)    
     toto = sumo - (11 * divo)
     totot=11-toto
     tol=str(totot)
     if totot == 10:
        tol = "k"
     print("dv=" + tol)
     if totot == 11:
        tol = "0"
     print("dv=" + tol)