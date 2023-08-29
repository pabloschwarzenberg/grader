def proyecto_genoma_humano(genoma):
    for i in genoma:
        if i!="a" or i!="c" or i!="t" or i!="g":
            return "secuencia incorrecta"
        else:
            return "secuencia correcta" 
print(proyecto_genoma_humano(input()))  
        