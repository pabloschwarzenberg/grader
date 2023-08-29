Fac = int(2);
Num = int(input("ingresar número: "))

while (Num != 1):
    if (Num % Fac == 0):
        print(str(Fac)+" ")
        Num = Num / Fac

    else:
        Fac = Fac + 1
if __name__ == "__main__":
    main()
      