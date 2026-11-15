import sys
import argparse
from lagring import las_in_servrar, exportera_till_csv
from kontroller import kontrollera_en_server, kontrollera_alla_servrar
from meny import kor_meny, skriv_ut_servrar, hitta_server, filtrera_miljo

def main():
    namn_list = las_in_servrar()

    parser = argparse.ArgumentParser(description="Hantera och kontrollera servrar")
    parser.add_argument("--lista", action="store_true", help="Visa alla servrar")
    parser.add_argument("--miljo", help="Filtrera servrar efter miljo")
    parser.add_argument("--kontrollera", help="Kontrollera en specifik server")
    parser.add_argument("--kontrollera-alla", action="store_true", help="Kontrollera alla servrar")
    parser.add_argument("--export", action="store_true", help="Exportera rapport som CSV")

    args = parser.parse_args()

    if args.lista:
        if args.miljo:
            filtrerad = filtrera_miljo(namn_list, args.miljo)
            skriv_ut_servrar(filtrerad)
        else:
            skriv_ut_servrar(namn_list)
        sys.exit(0)

    elif args.kontrollera:
        server = hitta_server(namn_list, args.kontrollera)
        if server != None:
            kontrollera_en_server(server, namn_list)
            print("Servern är kontrollerad!")
            # Returnera exit-kod 1 om servern inte svarar på ping
            if server["status"] == "down":
                sys.exit(1)
            else:
                sys.exit(0)
        else:
            print("Servern finns inte!")
            sys.exit(1)

    elif args.kontrollera_alla:
        kontrollera_alla_servrar(namn_list)
        print("Alla servrar är kontrollerade!")
        nagon_nere = False
        for x in namn_list:
            if x["status"] == "down":
                nagon_nere = True
        if nagon_nere == True:
            sys.exit(1)
        else:
            sys.exit(0)

    elif args.export:
        exportera_till_csv(namn_list)
        print("Rapport har exporterats till CSV!")
        sys.exit(0)

    else:
        kor_meny(namn_list)
        sys.exit(0)

if __name__ == "__main__":
    main()
