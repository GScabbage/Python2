import json
trainee= {'fname' : 'Garry', 'lname' : 'Garryson', 'Group' : {'G1' : 'ENG-69', 'G2' : 'ENG-84'}, 'Year' : '2k21'}
print (trainee)

with open('trianee.json', 'w') as file:
    json.dump(trainee, file, indent=4)
