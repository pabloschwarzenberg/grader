total_1=int(input("total de votos comuna 1: "))
total_2=int(input("total de votos comuna 2: "))
total_3=int(input("total de votos comuna 3: "))
provincia= total_1 + total_2 + total_3
obtenidos_1=int(input("total de votos obtenidos comuna 1: "))
obtenidos_2=int(input("total de votos obtenidos comuna 2: "))
obtenidos_3=int(input("total de votos obtenidos comuna 3: "))
if ((total_1/100)*80)<=obtenidos_1 :
    print("senadora electa")
elif ((total_2/100)*80)<=obtenidos_2 :
    print("senadora electa")
elif ((total_3/100)*80)<=obtenidos_3 :
    print("senadora electa")
elif (provincia/100)*70<=obtenidos_1 + obtenidos_2 :
    print("senadora electa")
elif (provincia/100)*70<=obtenidos_1 + obtenidos_3 :
    print("senadora electa")
elif (provincia/100)*70<=obtenidos_2 + obtenidos_3 :
    print("senadora electa")
elif (provincia/100)*40<=obtenidos_1 + obtenidos_3 + obtenidos_2 :
    print("senadora electa")
else :
    print("candidata perdedora")

      