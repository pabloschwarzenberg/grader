numerotelefonico=  int(input ("ingrese numero telefonico:  "))
llamado= int (input("ingrese hora del llamado:  "))

final= numerotelefonico % 1000
inicio= numerotelefonico //100000

if llamado  >= 0 and llamado <=7:
    print ("contestar")

elif final == 909 and llamado >= 8 and  llamado <= 14:
    print ("contestar")
elif llamado >= 8 and  llamado <= 14:
    print ("no contestar1")




elif llamado >= 17 or llamado <= 19:
    print ("no contestar2")

elif inicio== 877 and llamado >= 17 or llamado <= 19:
    print ("contestar")
