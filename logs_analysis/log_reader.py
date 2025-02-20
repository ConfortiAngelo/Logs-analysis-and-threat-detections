import os , re , glob



def read_logs(path):
    if os.path.exists(path):
        with open(path,'r') as file:
            return file.read()
    else:
        return "Error , el folder no existe!!"

# print(read_logs("C:/Users/angel/Desktop/CURSO"))
print(os.path.exists("C:/Users/angel/Desktop/CURSO"))
