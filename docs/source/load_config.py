import json

with open('../../config.json', 'r') as myfile:
    data = myfile.read()

object = json.loads(data)[0]

def parse():
    data = object['sections']
    res = []
    for key in data:
        for other_key in data[key]:
             res.append({other_key: data[key][other_key]})
    return (res)
class Project:
    def __init__(self):
        self.project_name = object['project_name']
        self.theme = object['theme']
        self.first_name = object['first_name']
        self.last_name = object['last_name']
        self.year = object['year']
        self.desc = object['desc']
        if object['active'] == 1:
            self.active = True
        else:
            self.active = False
        self.docs = parse()

instance = Project()