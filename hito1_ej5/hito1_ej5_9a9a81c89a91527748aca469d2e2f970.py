rut = input("Rut:")
#n1 = int(rut[0])
#n2 = int(rut[1])
#n3 = int(rut[2])
#n4 = int(rut[3])
#n5 = int(rut[4])
#n6 = int(rut[5])
#n7 = int(rut[6])
#n8 = int(rut[7])

if int(rut) >= 100000 and int(rut) <= 999999:
    n1 = int(rut[0])
    n2 = int(rut[1])
    n3 = int(rut[2])
    n4 = int(rut[3])
    n5 = int(rut[4])
    n6 = int(rut[5])

    sumatoria = (n1 * 7) + (n2 * 6) + (n3 * 5) + (n4 * 4) + (n5 * 3) + (n6 * 2)





if int(rut) >= 1000000 and int(rut) <= 9999999:
    n1 = int(rut[0])
    n2 = int(rut[1])
    n3 = int(rut[2])
    n4 = int(rut[3])
    n5 = int(rut[4])
    n6 = int(rut[5])
    n7 = int(rut[6])

    sumatoria = (n1 * 2) + (n2 * 7) + (n3 * 6) + (n4 * 5) + (n5 * 4) + (n6 * 3) + (n7 * 2)




if int(rut) >= 10000000 and int(rut) <= 99999999:
    n1 = int(rut[0])
    n2 = int(rut[1])
    n3 = int(rut[2])
    n4 = int(rut[3])
    n5 = int(rut[4])
    n6 = int(rut[5])
    n7 = int(rut[6])
    n8 = int(rut[7])

    sumatoria = (n1 * 3) + (n2 * 2) + (n3 * 7) + (n4 * 6) + (n5 * 5) + (n6 * 4) + (n7 * 3) + (n8 * 2)


        
if int(rut) >= 100000000 and int(rut) <= 999999999:
    n1 = int(rut[0])
    n2 = int(rut[1])
    n3 = int(rut[2])
    n4 = int(rut[3])
    n5 = int(rut[4])
    n6 = int(rut[5])
    n7 = int(rut[6])
    n8 = int(rut[7])
    n9 = int(rut[8])

    sumatoria = (n1 * 4) + (n2 * 3) + (n3 * 2) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2)


mod = 11
resultado = mod - (sumatoria -(mod * (sumatoria // mod)))
if int(resultado) == 11:
      print("dv=0")
if int(resultado) == 10:
      print("dv=k")
if int(resultado) != 10 and int(resultado) !=11:
      print("dv={}".format(resultado))

          
        
        
        