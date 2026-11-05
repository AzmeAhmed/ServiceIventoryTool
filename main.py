gold_server = {
    "namn": "power" , 
    "adress": "10.232.12.10" ,
    "miljo": "test" ,
    "roll": "fotboll" ,
    "status": "unknown" ,
    "senast_kontrollerad": "always"
}

namn_list = ["power"]

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


giltiga_miljoer = ["test"]

while True:

    gissning = input("Välj en miljö")

    if gissning in giltiga_miljoer:
        print("Korrekt miljö!")
        break
    else:
        print("Felaktigt miljö vald försök igen:")   
    

    

