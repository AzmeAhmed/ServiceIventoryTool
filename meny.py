from lagring import spara_servrar, exportera_till_csv
from kontroller import kontrollera_en_server, kontrollera_alla_servrar

def skriv_ut_servrar(server_lista):
    # :<15 pads each column to 15 characters for straight alignment
    print(f"{'NAMN':<15} {'ADRESS':<15} {'MILJO':<15} {'ROLL':<15} {'STATUS':<15} {'KONTROLLERAD':<15}")
    for x in server_lista:
        print(f"{x['namn']:<15} {x['adress']:<15} {x['miljo']:<15} {x['roll']:<15} {x['status']:<15} {x['senast_kontrollerad']:<15}")

def hitta_server(server_lista, sokt_namn):
    for x in server_lista:
        if x["namn"] == sokt_namn:
            return x
    return None

def filtrera_miljo(server_lista, miljo):
    filtrerad_lista = []
    for x in server_lista:
        if x["miljo"] == miljo:
            filtrerad_lista.append(x)
    return filtrerad_lista

def kor_meny(namn_list):
    giltiga_miljoer = ["test", "dev", "prod"]

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
            skriv_ut_servrar(namn_list)

        elif val == "2":
            vald_miljo = input("Vilken miljö vill du se: ").lower()
            filtrerad = filtrera_miljo(namn_list, vald_miljo)
            skriv_ut_servrar(filtrerad)

        elif val == "3":
            while True:
                nytt_namn = input("Välj ett namn: ")

                annat_namn = False

                # Check that the server name does not already exist
                for x in namn_list:
                    if x["namn"] == nytt_namn:
                        annat_namn = True

                if annat_namn == True:
                    print("Namnet redan registrerad testa igen:")

                else:
                    print("Nya namnet är nytt så den kan läggas till")
                    break

            while True:
                gissning = input("Välj en miljö: ").lower()

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
                # Extra confirmation is required before removing a prod server
                if server["miljo"] == "prod":
                    svar = input("Servern är i prod, är du säker (ja/nej): ").lower()
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
