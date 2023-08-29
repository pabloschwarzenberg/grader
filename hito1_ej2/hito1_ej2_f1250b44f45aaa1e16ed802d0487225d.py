numero =str(input("ingrese numero"))
hora =int(input("ingrese hora"))
nl =list(numero)
print(nl[5:8])

if 7>=hora>=0:
    print("CONTESTAR")
elif 14>hora and int(numero[5:8]) == 909 :
    print("CONTESTAR")
elif int(numero[5:8]) != 909:
    print("NO CONTESTAR")
elif 17>=hora>=19 and int(numero[0:3])!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")