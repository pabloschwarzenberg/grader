#Contestador de celular
nums = input("ingrese numero telefonico: ")
num = int(nums)
hora = int(input("ingrese hora de la llamada: "))
if num < 100000000 and num >= 10000000:
    if hora >= 0 and hora <= 7:
        print("CONTESTAR")
    elif hora >= 8 and hora <= 13:
        if nums.endswith("909"):
            print("CONTESTAR")
        else:
            print(" NO CONTESTAR")
    elif hora >= 14 and hora <= 16:
        print("NO CONTESTAR")
    elif hora >= 17 and hora <= 19:
        if nums.startswith("877"):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    elif hora >= 20 and hora <= 23:
        print("NO CONTESTAR")
else:
    print("poto")