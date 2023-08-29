def el_genomita(gen):
       kha="aAcCgGtT"
       for i in gen:
          pol = kha.find(i)
          if pol==-1:
            print("la secuencia",gen,"es incorrecta")
       if pol !=-1 :
        print("La secuencia",gen,"es correcta")
el_genomita(input())        
    