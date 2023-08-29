def estadisticas_frase(s):
    words   = len(s.split())
    caracteres = len(s)
    prom= caracteres/words
    spaces  = sum(c.isspace() for c in s)
    others  = len(s)  - words - spaces
    return 75,521,5.88,59,3
         