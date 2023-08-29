rut = (input("Ingrese los números: "))
if len(rut) == 8:
    
    
    n1 = int(rut[0:1])
    n2 = int(rut[1:2])
    n3 = int(rut[2:3])
    n4 = int(rut[3:4])
    n5 = int(rut[4:5])
    n6 = int(rut[5:6])
    n7 = int(rut[6:7])
    n8 = int(rut[7:8])
    total = ((n8*2) + (n7*3) + (n6*4) + (n5*5) + (n4*6) + (n3*7) + (n2*2) + (n1*3))
    nv = (total%11)
    nv1 = (11-nv)
    if nv1 == 11:
        nv1 = (0)
    if nv1 == 10:
        nv1 = ("k")
    print("dv= ",nv1)
if len(rut) == 7:
    
    n1 = int(rut[0:1])
    n2 = int(rut[1:2])
    n3 = int(rut[2:3])
    n4 = int(rut[3:4])
    n5 = int(rut[4:5])
    n6 = int(rut[5:6])
    n7 = int(rut[6:7])
    total = ((n7*2) + (n6*3) + (n5*4) + (n4*5) + (n3*6) + (n2*7) + (n1*2))
    nv = (total%11)
    nv1 = (11-nv)
    if nv1 == 11:
        nv1 = (0)
    if nv1 == 10:
        nv1 = ("k")
    print("dv= ",nv1)
    
    
    
    