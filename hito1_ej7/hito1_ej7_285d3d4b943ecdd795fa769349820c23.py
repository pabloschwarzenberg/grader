#Zodiaco
d = int(input("ingresa el dia de tu nacimiento como numero:"))
m = int(input("\ningresa el mes de tu nacimiento como numero:"))

if (21 <= d and m == 3) or (20 >= d and m == 4):
    print ("\naries\n")

elif (20 <= d and m == 4) or (21 >= d and m == 5):
    print ("\ntauro\n")
    
elif (21 <= d and m == 5) or (21 >= d and m == 6):
    print ("\ngeminis\n")
    
elif (21 <= d and m == 6) or (23 >= d and m == 7):
    print ("\ncancer\n")
    
elif (23 <= d and m == 7) or (23 >= d and m == 8):
    print ("\nleo\n")
    
elif (23 <= d and m == 8) or (23 >= d and m == 9):
    print ("\nvirgo\n")
    
elif (23 <= d and m == 9) or (23 >= d and m == 10):
    print ("\nlibra\n")
    
elif (23 <= d and m == 10) or (22 >= d and m == 11):
    print ("\nscorpio\n")
    
elif (23 <= d and m == 11) or (22 >= d and m == 12):
    print ("\nsagitario\n")
    
elif (22 <= d and m == 12) or (20 >= d and m == 1):
    print ("\ncapricornio\n")
    
elif (20 <= d and m == 1) or (19 >= d and m == 2):
    print ("\naquario\n")
    
elif (19 <= d and m == 2) or (21 >= d and m == 3):
    print ("\npiscis\n")