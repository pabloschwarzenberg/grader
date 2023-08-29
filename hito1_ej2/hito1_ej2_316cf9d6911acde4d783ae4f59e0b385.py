#Contestador de celular
numero = input("¿que numero es ?")
hora = int(input("¿ que hora es ?   "))
if hora >= 0 and hora <= 7 :
    print("CONTESTAR") 
elif hora <= 14 :
    if numero[5:8] ==  "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17  and hora <= 19:
    if numero[:3]  == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora >= 20  :
    print("NO CONTESTAR ")