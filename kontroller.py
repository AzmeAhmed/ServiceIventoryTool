import os
import subprocess
from datetime import datetime
from lagring import spara_servrar

def kontrollera_en_server(server, namn_list):
    if os.name == "nt":
        resultat = subprocess.run(["ping", "-n", "1", server["adress"]])
    else:
        resultat = subprocess.run(["ping", "-c", "1", server["adress"]])

    if resultat.returncode == 0:
        server["status"] = "up"
    else:
        server["status"] = "down"

    nu = datetime.now()
    tid = str(nu.year) + "-" + str(nu.month) + "-" + str(nu.day) + " " + str(nu.hour) + ":" + str(nu.minute)
    server["senast_kontrollerad"] = tid

    spara_servrar(namn_list)

def kontrollera_alla_servrar(namn_list):
    for server in namn_list:
        kontrollera_en_server(server, namn_list)
