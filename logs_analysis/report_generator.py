import json
from threat_detection import detections_threat
from log_reader import read_logs



def report_generate(attack_list,filename="report.json"):
    try:
        with open(filename,"r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        data = []  #Sino existe incio una lista vacia
    data.append(attack_list)
    with open(filename,"w") as file:
        json.dump(data,file,indent=4)

