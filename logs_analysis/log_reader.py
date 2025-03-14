import os

def read_logs(path):
    if os.path.exists(path):
        with open(path,'r') as file:
            for line in file:
                content = line.strip()
                yield content
    else:
        return "Error , el folder no existe!!"

path = "/home/angelo/Escritorio/CURSO/Cibersecurity/Logs analysis and threat detection/data/sample_log_1.log"
path_2 = "/home/angelo/Escritorio/CURSO/Cibersecurity/Logs analysis and threat detection/data/sample_log_2.log"

for line in read_logs(path_2):
    print(line)