def adn (secuencia):
    for letra in secuencia:
        for letra in ("actg"):
            if not letra.lower() not in ("bdefhijklmnopqrsuvwxyz") and letra in ("actg"):
                return("secuencia correcta")
            elif letra in ("actg") and letra not in ("bdefhijklmnopqrsuvwxyz") :
                return("secuencia incorrecta")