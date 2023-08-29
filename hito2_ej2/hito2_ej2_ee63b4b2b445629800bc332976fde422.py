def adn(secuencia):
   for letra in secuencia:
      for letra in ("actg"):
          if not letra.lower()  in ("bdefhijklmnopqrsuvwxyz") and letra in ("actg"):
              return("correcta")
          else:
              return("incorrecta")
