class Twitter:
  # Atributo que almacena los trending topics como una lista de tuplas (hashtag, frecuencia)
  trending_topics = []

  # Método que recibe un tweet como string y actualiza la lista de trending topics
  def tweet(self, mensaje):
    # Verificar que el tweet no supere los 140 caracteres
    if len(mensaje) > 140:
      print("El tweet es demasiado largo")
      return
    # Imprimir el tweet
    print(mensaje)
    # Dividir el tweet por espacios
    palabras = mensaje.split()
    # Recorrer cada palabra del tweet
    for palabra in palabras:
      # Verificar si la palabra empieza con #
      if palabra.startswith("#"):
        # Quitar el # para obtener el hashtag
        hashtag = palabra[1:]
        # Buscar el hashtag en la lista de trending topics
        encontrado = False
        for i in range(len(self.trending_topics)):
          # Si el hashtag ya está en la lista, aumentar su frecuencia en uno
          if self.trending_topics[i][0] == hashtag:
            self.trending_topics[i] = (hashtag, self.trending_topics[i][1] + 1)
            encontrado = True
            break
        # Si el hashtag no está en la lista, agregarlo con frecuencia uno
        if not encontrado:
          self.trending_topics.append((hashtag, 1))
    # Ordenar la lista de trending topics de mayor a menor frecuencia
    self.trending_topics.sort(key=lambda x: x[1], reverse=True)
    # Mostrar los tres hashtags más repetidos hasta el momento
    print("Los tres hashtags más repetidos son:")
    for i in range(min(3, len(self.trending_topics))):
      print(self.trending_topics[i][0], ":", self.trending_topics[i][1])
