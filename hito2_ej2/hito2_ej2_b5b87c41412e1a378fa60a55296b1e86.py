def genoma(genoma):
    val_a = 0
    val_c = 0
    val_t = 0
    val_g = 0
    val_otro = 1
    val_correcto = 0
    for i in genoma:
        if i == 'A' or i =='a':
            val_a = 1
        elif i == 'C' or i =='c':
            val_c =1
        elif i == 'T' or i =='t':
            val_t =1
        elif i == 'G' or i =='g':
            val_g =1
        elif i != 'a' or i != 'A' or i != 'c' or i != 'C' or i != 't' or i != 'T' or i != 'g' or i != 'G':
            val_otro = 0


        if val_a == 1 and val_t == 1 and val_c == 1 and val_g == 1 and val_otro == 1:
            val_correcto = 1
        else:
           val_correcto = 0

    if val_correcto == 1:
        print("Secuencia correcta")
    else:
        print("Secuencia incorrecta")


var_genoma = input("Ingrese secuencia\n")
genoma(var_genoma)