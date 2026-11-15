import sys
from lagring import las_in_servrar, spara_servrar, exportera_till_csv
from kontroller import kontrollera_en_server, kontrollera_alla_servrar

def hitta_server(server_lista, sokt_namn):
    for x in server_lista:
        if x["namn"] == sokt_namn:
            return x
    return None

namn_list = las_in_servrar()
giltiga_miljoer = ["test", "dev", "prod"]

if len(sys.argv) == 1:
    while True:
        print("\n1. Visa alla servrar")
        print("2. Visa servrar i en viss miljö")
        print("3. Lägga till en server")
        print("4. Ta bort en server")
        print("5. Kontrollera en server")
        print("6. Kontrollera alla servrar")
        print("7. Exportera rapport som CSV")
        print("8. Avsluta")

        val = input("Välj ett alternativ: ")

        if val == "1":
            for x in namn_list:
                print(x)

        elif val == "2":
            vald_miljo = input("Vilken miljö vill du se: ")
            for x in namn_list:
                if x["miljo"] == vald_miljo:
                    print(x)

        elif val == "3":
            while True:
                nytt_namn = input("Välj ett namn: ")

                annat_namn = False

                for x in namn_list:
                    if x["namn"] == nytt_namn:
                        annat_namn = True

                if annat_namn == True:
                    print("Namnet redan registrerad testa igen:")

                else:
                    print("Nya namnet är nytt så den kan läggas till")
                    break

            while True:
                gissning = input("Välj en miljö: ")

                if gissning in giltiga_miljoer:
                    print("Korrekt miljö!")
                    break
                else:
                    print("Felaktigt miljö vald försök igen:")

            ny_roll = input("Välj en roll: ")
            ny_adress = input("Välj en adress: ")

            fresh_server = {
                "namn": nytt_namn,
                "adress": ny_adress,
                "miljo": gissning,
                "roll": ny_roll,
                "status": "unknown",
                "senast_kontrollerad": ""
            }

            namn_list.append(fresh_server)
            print("Den nya servern har lagts till! ")
            spara_servrar(namn_list)

        elif val == "4":
            ta_bort = input("Vilken server vill du ta bort: ")
            server = hitta_server(namn_list, ta_bort)
            if server != None:
                if server["miljo"] == "prod":
                    svar = input("Servern är i prod, är du säker (ja/nej): ")
                    if svar == "ja":
                        namn_list.remove(server)
                        spara_servrar(namn_list)
                        print("Servern har tagits bort!")
                    else:
                        print("Avbrutet!")
                else:
                    namn_list.remove(server)
                    spara_servrar(namn_list)
                    print("Servern har tagits bort!")
            else:
                print("Servern finns inte!")

        elif val == "5":
            koll_namn = input("Vilken server vill du kontrollera: ")
            server = hitta_server(namn_list, koll_namn)
            if server != None:
                kontrollera_en_server(server, namn_list)
                print("Servern är kontrollerad!")
            else:
                print("Servern finns inte!")

        elif val == "6":
            kontrollera_alla_servrar(namn_list)
            print("Alla servrar är kontrollerade!")

        elif val == "7":
            exportera_till_csv(namn_list)
            print("Rapport har exporterats till CSV!")

        elif val == "8":
            print("Programmet avslutas")
            break

        else:
            print("Ogiltigt val, försök igen!")
