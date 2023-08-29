while True:
    try:
        n_t=int(input("Ingresar numero: "))
        time=int(input("Ingresar la hora de la llamada: "))
        a=n_t%1000
        b=n_t//100000
        if (n_t > 1000000 and n_t <= 99999999) and (time >= 0 and time ):
            if time >= 0 and time <= 7:
                print("CONTESTAR")
                break
            if (time < 14 and time > 7) and a!= 909:
                print("NO CONTESTAR")
                break
            if (time < 14 and time > 7) and a == 909:
                print("CONTESTAR")
                break
            if (time > 17 and time < 19) and b!= 877:
                print("CONTESTAR")
                break
            if (time > 17 and time < 19) and b== 877:
                print("NO CONTESTAR")
                break
            if time > 19 and time < 24:
                print("NO CONTESTAR")
                break
    except:
        print("Numero no valido")
    
          