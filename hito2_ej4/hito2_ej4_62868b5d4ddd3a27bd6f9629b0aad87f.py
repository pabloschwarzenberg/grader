lista = []
wallet = 0
while True:
      respuesta=input("¿que deseas hacer?")
      p1=[1,"Pokemon X",33.77]
      p2=[2,"Nintendo XL",203]
      p3=[3,"Mario Kart 7",27.58]
      p4=[4,"PlayStation 4",348.00]
      p5=[5,"FIFA 16",51.19]
      #funcion "ver"
      if respuesta=="ver":
            print("".join(lista))
      elif respuesta=="checkout":
            if listabuscar.find("Pokemon X")!=-1 and listabuscar.find("Nintendo XL")!=-1 and listabuscar.find("Mario Kart 7")!=-1:
                  wallet-=52.87
            elif listabuscar.find("PlayStation 4")!=-1 and listabuscar.find("FIFA 16")!=-1:
                  wallet-=59.8785
            wallet=round(wallet,1)
            print("precio final:",wallet)
            break
      else:
            lista_respuesta=respuesta.split(",")
            producto=int(lista_respuesta[0])
            cantidad=int(lista_respuesta[1])
            cantidad=int(cantidad)

            nombres=[
                  "Pokemon X",
                  "Nintendo XL",
                  "Mario Kart 7",
                  "PlayStation 4",
                  "FIFA 16"
            ]
            numeros=[1,2,3,4,5]
            precios=[33.77,203,27.58,348.00,51.19]
            lista+=str(cantidad)+"  "+nombres[int(producto)-1]+"   $"+ str(cantidad*precios[int(producto)-1])+"""
"""
            listabuscar=""
            listabuscar+="".join(lista)
            wallet+=float((cantidad*precios[int(producto)-1]))
            wallet=wallet



