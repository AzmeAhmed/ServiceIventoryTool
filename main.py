gold_server = {
    "namn": "power" , 
    "adress": "10.232.12.10" ,
    "miljo": "test" ,
    "roll": "fotboll" ,
    "status": "unknown" ,
    "senast_kontrollerad": "always"
}

namn_list = [gold_server]

while True:
    nytt_namn = input("Välj ett namn")

    annat_namn = False

    for x in namn_list: 
        if x["namn"] == nytt_namn:
            annat_namn = True   

    if annat_namn == True:
        print("Namnet redan registrerad testa igen:")

    else:
        print("Nya namnet är nytt så den kan läggas till")
        break


giltiga_miljoer = ["test" , "dev" , "prod"]
giltiga_statusar = ["unknown" , "down" , "up"]

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
    "senast_kontrollerad": "always"
}

namn_list.append(fresh_server)
print("Den nya servern har lagts till! ")
    

    

