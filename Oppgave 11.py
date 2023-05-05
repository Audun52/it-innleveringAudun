import csv
import matplotlib.pyplot as plt



filnavn = "oppgave11.csv"

with open(filnavn, encoding = "utf-8-sig",) as file:
    filinnhold = csv.reader(file, delimiter = ";")
    
    overskrift = next(filinnhold)
    
    matT = 0 # Skal regne ut total pris brukt på mat
    strømmT = 0 # Skal regne ut total pris brukt på strømm
    jan = 0 # Skal regne ut penger brukt i Januar
    feb = 0 # Skal regne ut penger brukt i Februar
    mars = 0 # Skal regne ut penger brukt i Mars
    peng = [] # Skal bruke denne til graftegneren 
    
    for rad in filinnhold:
        if rad[1] == "mat":
            matT += int(rad[2]) # plusser på matT hvis den er skrevet opp som mat
        if rad[1] == "strøm":
            strømmT += int(rad[2]) # pluser på strømmT hvis den er skrevet opp som strømm
        if rad[0][3:5] == "01": # Kjekker om datoen er i Januar
            jan += int(rad[2])
        if rad[0][3:5] == "02":
            feb += int(rad[2])
        if rad[0][3:5] == "03":
            mars += int(rad[2])
    
    peng.append(jan)
    peng.append(feb)
    peng.append(mars) # Samler alle prisene i en liste for grafen
        
#%% a
print(f"Familien Rosendal har brukt {matT}kr på mat og {strømmT}kr på strømm")
print("")
#%%b
print(f"Familien Rosendal brukte {jan}kr i Januar, {feb}kr i Februar og {mars}kr i Mars")
print("")
#%%
x = ["jan", "feb", "mar"]

plt.bar(x, peng, color = "indigo") # likte ikke blå fargen så jeg endra den
plt.grid(axis="y") # puttet på linjer i y aksen sånn at det er lettere å sammenligne
plt.title("Pengeforbruk til familien Rosendal fra Januar til Mars")
plt.show()
#%%

dato = input("Hva er datoen?  ")
typee = input("Er det mat eller strømm pris?  ")
kromer = input("Hvor mange kroner brukte du?  ")
sted = input("Hvor brukte du pengene?  ")
with open(filnavn, "a", encoding = "utf-8-sig") as file:
    
    info = [dato, ";", typee, ";", kromer, ";", sted] # Samler all informasjonen som brukeren putter inn
    
    tekst = ""
    for i in info: # Gjør informasjonen til en stor string
        tekst+=i
    
    file.write(tekst) # skriver inn den store stringen
    
with open(filnavn, encoding = "utf-8-sig",) as file:
    filinnhold = csv.reader(file, delimiter = ";")
    
    for rad in filinnhold:
        print(rad) # leser ut hele greia

#Har problemer med å fjerne gamle ting jeg putta inn, nå ser det ut som lister fylt med tomme stringer?