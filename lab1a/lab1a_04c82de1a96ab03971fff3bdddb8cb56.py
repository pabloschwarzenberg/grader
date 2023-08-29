#Elecciones
tv1=int(input("Ingrese total de votos comuna 1: "))
tv2=int(input("Ingrese total de votos comuna 2: "))
tv3=int(input("Ingrese total de votos comuna 3: "))
iv1=int(input("Ingrese total de votos para Isabel en la comuna 1: "))
iv2=int(input("Ingrese total de votos para Isabel en la comuna 2: "))
iv3=int(input("Ingrese total de votos para Isabel en la comuna 3: "))
if iv1 >= 80*tv1/100 or iv2 >= 80*tv1/100 or iv3 >= 80*tv1/100:
 print("senadora electa")
if iv1+iv2 >= 70*(tv1+tv2)/100 or iv1+iv3 >= 70*(tv1+tv3)/100 or iv2+iv3 >= 70*(tv2+tv3)/100:
 print("senadora electa")
if iv1+iv2+iv3 >= 40*(tv1+tv2+tv3)/100:
 print("senadora electa")
print("candidata perdedora")