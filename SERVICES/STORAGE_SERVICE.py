import json
#Function for loading data
def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#Funtion for saving data
def save_data(file_path, data):
    with open (file_path,"w") as file:
        json.dump(data, file, indent=4)
