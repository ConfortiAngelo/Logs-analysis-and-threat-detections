import os

def read_logs(path):
    if os.path.exists(path):
        with open(path,'r') as file:
            for line in file:
                content = line.strip()
                yield content
    else:
        return "Error , el folder no existe!!"


# for line in read_logs(path_2):
#     print(line)