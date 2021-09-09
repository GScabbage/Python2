import json



with open('trianee.json', 'r') as file:
    trainee=json.load(file)

for key, value in trainee.items():
    print (f"{key}= {value}")

trainee ['Year'] = [2020,2021,2022]

with open('trianee.json', 'w') as file:
    json.dump(trainee, file, indent=4)
