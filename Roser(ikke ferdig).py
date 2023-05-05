class Rose:
    def __init__(self, farge, pris, blomstringsTid):
        self.farge = farge
        self.pris = pris
        self.tid = blomstringsTid
        
class BuskRose(Rose):
    def __init__(self, farge, pris, blomstringsTid, bredde, høyde):
        super().__init__(farge, pris, blomstringsTid)
        self.bredde = bredde
        self.høyde = høyde
        
    def visInfo(self):
        print(f"Denne buskrosen er {self.høyde}cm høy og {self.bredde}cm bred. Den er {self.farge} og den koster {self.pris}kr. blomstringstiden er {self.tid} ")

class KlatreRose(Rose):
    def __init__(self, farge, pris, blomstringsTid, lengde, støttekrav, vokseMønster):
        super().__init__(farge, pris, blomstringsTid)
        self.lengde = lengde
        self.støtte = støttekrav
        self.mønster = vokseMønster
    
    def visInfo(self):
        print(f"denne klatreosen har en høyde på {self.lengde}")
        
class StilkRose(Rose):
    def __init__(self, farge, pris, blomstringsTid, lengde, antallBlomsterPerStilk, duft):
        super().__init__(farge, pris, blomstringsTid)
        self.lengde = lengde
        self.antall = antallBlomsterPerStilk
        self.duft = duft
        
class Innboks:
    def __init__(self, roser, antall):
        self.roser = roser
        self.antall = antall

class Kunde:
    def __init__(self, navn, kontaktinformasjon, kjøpehistorikk):
        self.navn = navn
        self.kontakt = kontaktinformasjon
        self.historie = kjøpehistorikk
        
a = BuskRose("rød", "200", "mai til april", "20", "20")
a.visInfo()
