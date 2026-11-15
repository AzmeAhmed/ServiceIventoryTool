# ServiceIventoryTool

Ett program i Python för att hålla koll på servrar, se om de svarar på ping och spara allt i en JSON-fil. Det går också att spara ut en rapport som CSV.

## Vad som krävs
* Python 3 (inga extra paket behövs, bara vanliga standardbibliotek i Python)
* Windows, Mac eller Linux som har kommandot ping

## Hur projektet är uppbyggt
* main.py - Startar programmet och läser av flaggor från terminalen med argparse.
* meny.py - Innehåller textmenyn och funktioner för att visa, söka och filtrera servrar.
* lagring.py - Läser in och sparar servrar i JSON och skapar CSV-rapporter i mappen rapporter.
* kontroller.py - Pingar en eller alla servrar och uppdaterar status och tid.
* servrar.json - Filen där alla servrar sparas.

## Hur man startar programmet

Programmet kan köras på två sätt i terminalen:

### 1. Textmeny (utan flaggor)
Kör bara filen utan några extra argument:
```bash
python main.py
```

Då kommer en meny upp med 8 val:
1. Visa alla servrar
2. Visa servrar i en viss miljö (test, dev eller prod)
3. Lägga till en server
4. Ta bort en server (frågar en extra gång om den ligger i prod)
5. Kontrollera en server
6. Kontrollera alla servrar
7. Exportera rapport som CSV
8. Avsluta

### 2. Kommandoraden (med flaggor)
Man kan också köra kommandon direkt i terminalen:

```bash
python main.py --lista
python main.py --lista --miljo prod
python main.py --kontrollera web01
python main.py --kontrollera-alla
python main.py --export
python main.py --help
```

Programmet skickar tillbaka exit-kod 0 om allt gick bra och exit-kod 1 om en server inte finns eller inte svarar på ping.

## Miljövariabel (INVENTORY_DATAFIL)
Som standard sparas allt i servrar.json. Om man vill använda en annan fil kan man ändra miljövariabeln INVENTORY_DATAFIL innan man kör programmet.

Windows (PowerShell):
```powershell
\$env:INVENTORY_DATAFIL="test.json"
python main.py
```

Mac eller Linux:
```bash
export INVENTORY_DATAFIL="test.json"
python main.py
```
