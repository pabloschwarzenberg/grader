def complementary_strand(self, strand):
        ''' Takes a DNA strand string and finds its opposite base pair match. '''
        strand = strand.upper()
        newstrand = ""
        for i in range(0, len(strand)):
            if strand[i] == "T":
                newstrand += "A"

            if strand[i] == "A":
                newstrand += "T"

            if strand[i] == "G":
                newstrand += "C"

            if strand[i] == "C":
                newstrand += "G"

        return newstrand