def valida_secuenciaADN(string):

    for dato in string:
        for letraADN in "ACTGactg":
            if dato == letraADN:
                return "La secuencia "+string+" es correcta"
            else:
                return "La secuencia "+string+" es incorrecta"


if __name__ == "__main__":
    var = valida_secuenciaADN("actgb")
    print(var)