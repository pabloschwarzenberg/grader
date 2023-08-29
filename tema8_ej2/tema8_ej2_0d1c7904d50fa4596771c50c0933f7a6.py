def buscarTodas(a,b):
    Letra_Ronda = ""
    for pos,char in enumerate(a):
      if(char == b):
        Letra_Ronda=Letra_Ronda + str(pos) + " "
    Letra_Ronda=Letra_Ronda.rstrip(Letra_Ronda[-1])
    return Letra_Ronda
    pass

if __name__ == "__main__":
    a = input()
    b=input()
    print(buscarTodas(a,b))
    pass           