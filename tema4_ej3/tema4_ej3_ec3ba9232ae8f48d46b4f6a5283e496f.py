def jerigonzo(y):
 z=""
 for i in y:
    if i=="a" or i=="e" or i=="i"or i=="o" or i=="u":
       z+=i+"p"+i

    else:
        z+=i
 return z       

if __name__ == "__main__":
    y=(input("ingrese una palabra:"))
    print(jerigonzo(y))