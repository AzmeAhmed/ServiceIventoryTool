import json
import os

def ladda_filnamn():
    if "INVENTORY_DATAFIL" in os.environ:
        return os.environ["INVENTORY_DATAFIL"]
    else:
        return "servrar.json"

def las_in_servrar():
    filnamn = ladda_filnamn()
    if os.path.exists(filnamn):
        min_fil = open(filnamn, "r")
        servrar = json.load(min_fil)
        min_fil.close()
        return servrar
    else:
        return []

def spara_servrar(namn_list):
    filnamn = ladda_filnamn()
    min_fil = open(filnamn, "w")
    json.dump(namn_list, min_fil)
    min_fil.close()

def exportera_till_csv(namn_list):
    if not os.path.exists("rapporter"):
        os.makedirs("rapporter")
        
    csv_namn = "rapporter/inventering_export.csv"
    
    min_fil = open(csv_namn, "w")
    min_fil.write("namn,adress,miljo,roll,status,senast_kontrollerad\n")
    
    for server in namn_list:
        rad = server["namn"] + "," + server["adress"] + "," + server["miljo"] + "," + server["roll"] + "," + server["status"] + "," + server["senast_kontrollerad"] + "\n"
        min_fil.write(rad)
        
    min_fil.close()
