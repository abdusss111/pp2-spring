import json

json_file_path = '/Users/abdussalamabdurakhimov/Desktop/code/pp2/summer/week4/json/data.json'

with open(json_file_path, 'r') as file:
    data = json.load(file)  
    

print(data)


