# Skriftlig redogörelse

## 1. Tre olika konstruktioner i koden
* Villkor (if/else): I kontroller.py i funktionen kontrollera_en_server använder jag if resultat.returncode == 0: för att kolla om ping fungerade. Om uttrycket efter if är sant körs koden under och sätter status till "up", annars körs else-delen som sätter status till "down".
* Loop (for): I meny.py i funktionen kor_meny under val 3 har jag en loop for x in namn_list: som går igenom alla servrar i listan en efter en. Den kollar med if x["namn"] == nytt_namn: om namnet redan finns så att man inte kan lägga till två servrar med samma namn.
* Funktion med parametrar och return: I meny.py har jag funktionen hitta_server(server_lista, sokt_namn) som tar emot listan med servrar och namnet man söker efter. Den loopar igenom listan och använder return x för att skicka tillbaka hela servern när den hittar rätt namn, eller return None om den inte finns.

## 2. Varför en lista med dictionaries passar och vilka datatyper som används
En lista passar bra eftersom det är enkelt att lägga till nya servrar med .append(), ta bort med .remove() och loopa igenom alla servrar på samma gång som i kontrollera_alla_servrar i kontroller.py. Varje server är en dictionary eftersom man kan ge varje värde ett tydligt nyckelnamn som "namn", "adress" och "status" istället för att gissa indexnummer. I min kod (till exempel i fresh_server i meny.py) är alla värden i en server strängar (str), som "web01", "prod" och "unknown".

## 3. Varför data sparas i JSON men exporteras som CSV
Jag sparar servrarna i JSON i lagring.py (las_in_servrar och spara_servrar) eftersom JSON fungerar precis som listor och dictionaries i Python, så det är lätt att ladda in datan igen utan att tappa strukturen. När jag exporterar en rapport i exportera_till_csv i lagring.py använder jag CSV eftersom det är ett enkelt textformat med kommatecken som man kan öppna direkt i Excel för att se en tabell.

## 4. Hur programmet är uppdelat i moduler och funktioner
Jag har delat upp programmet i fyra filer så att varje fil har sitt eget ansvar och koden blir lättare att läsa:
* main.py startar programmet i main() och läser av flaggor från terminalen med argparse (som --lista och --kontrollera). Om inga flaggor skrivs in startar den textmenyn.
* meny.py sköter textmenyn i kor_meny samt funktioner för att skriva ut tabellen (skriv_ut_servrar), leta upp en server (hitta_server) och filtrera miljö (filtrera_miljo).
* lagring.py sköter filerna, alltså att läsa och spara JSON (las_in_servrar, spara_servrar), kolla miljövariabeln (ladda_filnamn) och skapa CSV-rapporter (exportera_till_csv).
* kontroller.py sköter ping-kontrollerna för en server (kontrollera_en_server) eller alla servrar (kontrollera_alla_servrar) och sparar status och tid.

## 5. Moduler från standardbiblioteket och vad de används till
* json används i lagring.py (json.load och json.dump) för att läsa och spara Python-listan i JSON-filen.
* os används i lagring.py för att kolla miljövariabeln INVENTORY_DATAFIL (os.environ) och skapa mappen rapporter (os.makedirs), samt i kontroller.py (os.name) för att se om datorn kör Windows eller Mac/Linux.
* pathlib (Path) används i lagring.py i las_in_servrar för att kolla om JSON-filen finns (filnamn.exists()) innan den öppnas.
* datetime används i lagring.py och kontroller.py (datetime.now()) för att hämta datum och tid till CSV-filnamnet och senast_kontrollerad.
* subprocess används i kontroller.py (subprocess.run) för att köra ping-kommandot i terminalen från Python.
* argparse används i main.py för att läsa av flaggor i kommandoraden som --lista, --miljo och --kontrollera och skapa --help.
* sys används i main.py (sys.exit(0) och sys.exit(1)) för att avsluta programmet med rätt exit-kod beroende på om allt gick bra eller om en server var nere eller saknades.

## 6. Tre exempel på god praxis i koden
* Ingen duplicerad kod: Istället för att skriva samma for-loop för att filtrera miljö i både meny.py och main.py har jag lagt den i en egen funktion filtrera_miljo i meny.py som båda använder. Då slipper man ändra på två ställen om något ska justeras.
* Startpunkt med if __name__ == "__main__": Längst ner i main.py har jag denna rad innan main() körs. Det gör att programmet bara startar när man kör main.py direkt och inte om en annan fil importerar något därifrån.
* Tydliga namn utan å, ä, ö och en .gitignore-fil: Alla variabler och funktioner är skrivna med små bokstäver och understreck utan å, ä, ö (som las_in_servrar och vald_miljo) för att slippa strul på olika datorer. Jag har också en .gitignore som hindrar tillfälliga filer som __pycache__/ och mappen rapporter/ från att komma med till GitHub.

## 7. Källor och hjälpmedel jag har använt
Under projektet har jag använt kursmaterialet, övningarna och föreläsningarna för att förstå hur man jobbar med filer, funktioner, argparse och hur Git-flödet med branches och Pull Requests fungerar. I början kollade jag även på en del YouTube-videor för att bättre förstå hur vissa delar hänger ihop, som att jobba med JSON-filer, funktioner i flera filer och hur Git och GitHub funkar i praktiken. Jag har också använt W3Schools för att slå upp syntax och enkla exempel på hur moduler som subprocess, datetime och pathlib används. Utöver det har jag använt ett AI-verktyg som hjälp för att förstå logiken bakom de olika G-kraven, få förklaringar på hur koden hänger ihop och få tips på hur jag kunde dela upp koden i flera moduler.

