import json

with open('../../config.json', 'r') as myfile:
    data = myfile.read()

object = json.loads(data)[0]

# item -  module_name: ([operations], [errors])
# result: list[item]
def parse():
    data = object['sections']
    # print(data)
    res = []
    for key in data:
        # print(data[key]['errors'])
        # print(data[key])
        # d = {}
        # print(data[key]['errors'])
        for other_key in data[key]:
             res.append({other_key: data[key][other_key]})
        # t = [data[key]['operations'], data[key]['errors']]
        # res.append({key: t})
        # print(data[key]['operations'])
        # d[data[key]['operations']] = ("default", "text")
        # res.append(d)
        # d = {key: t}
        # res.append(d)
        # res(data[key]) = ('default', 'text')
    # print(res)
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

parse()

instance = Project()