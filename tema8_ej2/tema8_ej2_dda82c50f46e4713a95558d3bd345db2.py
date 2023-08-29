def buscarTodas(a, b):
    contador = 0
    saltador = 0
    algo = ""
    for i in range(a.count(b)):

        algo = algo + str(a.index(b, saltador)) + " "

        if saltador == 0:
            saltador += 1
        saltador = saltador + 4
    algo = algo[0:len(algo) -1] 
    return algo

    


           