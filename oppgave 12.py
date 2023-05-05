# Eksempel på hva som kan være feil i koden
class Person():
    def __init__(self, navn):
        self.navn = navn
        self.status = "singel"
        self.brud = "ingen"
        
    def gifteMeg(self, brud):
        if self.status == "singel": # kjekker ikke om bruden sin status er singel
            self.status = f"gift med {brud.navn}" # self gifter seg med brud men ikke omvendt
            self.brud = brud.navn
        else:
            print(f"Beklager {brud.navn} jeg er allerede gift med {self.brud}") # Går bar en vei men ikke den andre
            
    def visStatus(self):
        print(f"Jeg er {self.status}")

def hovedprogram():
    brad = Person("Brad Pitt")
    brad.visStatus()
    
    angie = Person("Angelina Jolie")
    brad.gifteMeg(angie)
    brad.visStatus()
    
    jo = Person("Jo By")
    brad.gifteMeg(jo)
    
    jo.gifteMeg(brad)
    jo.visStatus()
    
hovedprogram()

print("")
# under er ett eksempel på en kode som ikke har den samme feilen
class Person2():
    def __init__(self, navn):
        self.navn = navn
        self.status = "singel"
        self.brud = "ingen"
        
    def gifteMeg(self, brud):
        if self.status == "singel" and brud.status == "singel": # kjekker både om self er singel og om bruden er singel
            self.status = f"gift med {brud.navn}"
            brud.status = f"gift med {self.navn}" # begge to blir gift sammen
            self.brud = brud.navn
            brud.brud = self.navn # begge to får den andre som partner
        elif self.status != "singel": 
            print(f"Beklager {brud.navn} jeg er allerede gift med {self.brud}")
        else: # Har to avslå meldinger som kommer anpå hvem som er gift
            print(f"Beklager {self.navn} jeg er allerede gift med {brud.brud}")
            
    def visStatus(self):
        print(f"Jeg er {self.status}")

def hovedprogram2():
    brad = Person2("Brad Pitt")
    brad.visStatus()
    
    angie = Person2("Angelina Jolie")
    brad.gifteMeg(angie)
    brad.visStatus()
    
    jo = Person2("Jo By")
    brad.gifteMeg(jo)
    
    jo.gifteMeg(brad)
    jo.visStatus()
    
hovedprogram2()