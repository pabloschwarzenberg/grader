import random
Ls=["murcielago"," mantarraya", "artropodo", "berenjena","stradivarius","onomatopeya","castor","gato","pez"]
def ocultar_letras(palabra,cantidad):
    palabra=random.choice(Ls)
    letra=random.choice(palabra)
    n=random.randint(0,len(palabra))
    r=palabra.replace(letra,"_")
    print(r)
    print(palabra.replace(letra,"_"))
       
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra

if __name__ == "__main__":
    pass
         