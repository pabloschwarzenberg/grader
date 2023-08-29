def jerigonzo(string):
    jeri=""
    for i in string:
        jeri+=i
        if i=="a" or i =="e" or i =="i" or i =="o" or i =="u":
            jeri+="p"+i
    return jeri
if __name__ == "_main_":
    palabra=str(input("Escriba su palabra: "))
    print("Su palabra en jerigonzo es: ",jerigonzo(palabra))
    pass
         