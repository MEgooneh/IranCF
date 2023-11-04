import json
from core.cf_link_generator import generate_link_for_problem

with open('table.json', 'r') as f :
    data = json.load(f)

lst = []

for i in data.keys() :
    contest, index = i.split(' ')
    url = generate_link_for_problem(i)
    score = format(data[i], ".2f")
    lst.append({"contest":contest,"id":index,"url":url,"score":score})

with open('detailed.json', 'w') as f:
    json.dump(lst, f , indent=4)