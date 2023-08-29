es_primo = int(input("ingresa numero : "))
primo  = es_primo%2
primo2 = es_primo%3
if (primo==0) or (primo2 == 0):
    print("False")
else:
    print("True")
