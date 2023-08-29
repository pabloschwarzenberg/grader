numero= input("ingrese un numero telefomico")
hora= int(input("ingrese una hora"))
termino=numero[5:8]
comienzo = numero[0:3]   
   
   
   
   
if hora>=0 and hora<=7:
    print("contestar")
elif termino== "909" and hora <14:
    print("contestar")
elif hora <14:
    print("no contestar ")
elif comienzo== "877" and hora>17 and hora<19:
    print("no contestar")
elif hora>17 and hora<19:
    print("contestar ")
elif hora>19:
    print("no contestar")
    