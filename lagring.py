import json
import os
from pathlib import Path
from datetime import datetime


def ladda_filnamn():
    # Check if a custom data file is set via environment variable
    if "INVENTORY_DATAFIL" in os.environ:
        return os.environ["INVENTORY_DATAFIL"]
    else:
        return "servrar.json"

def las_in_servrar():
    filnamn = Path(ladda_filnamn())
    if filnamn.exists():
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
    # Create the rapporter folder if it does not exist
    if not os.path.exists("rapporter"):
        os.makedirs("rapporter")
        
    nu = datetime.now()
    tid = nu.strftime("%Y-%m-%d_%H%M")
    csv_namn = "rapporter/inventering_" + tid + ".csv"
    
    min_fil = open(csv_namn, "w")
    min_fil.write("namn,adress,miljo,roll,status,senast_kontrollerad\n")
    
    for server in namn_list:
        rad = server["namn"] + "," + server["adress"] + "," + server["miljo"] + "," + server["roll"] + "," + server["status"] + "," + server["senast_kontrollerad"] + "\n"
        min_fil.write(rad)
        
    min_fil.close()
