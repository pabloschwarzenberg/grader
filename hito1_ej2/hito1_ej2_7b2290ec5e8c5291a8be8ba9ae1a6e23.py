#Contestador de celular
num_tel = int(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese hora de la llamada: "))

num_tel_len1 = len(str(num_tel))

if num_tel_len1 < 8 or num_tel_len1 > 9:
    print("El numero telefonico debe ser de 8 cifras")
    #exit()

if hora < 0 or hora > 23:
    print("La hora de la llamada debe ser entre 0 a 23hrs.")
    #exit()    

if hora >= 0 and hora <= 7:
    print("CONTESTAR")
    #exit() 

num_to_str = (str(num_tel))
final_num = num_to_str[5:8]
inicio_num = num_to_str[0:3]
#print(final_num)

if hora > 7 and hora < 14:
    if final_num == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
    #exit()
elif hora >= 17 and hora <= 19:
    if inicio_num == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")