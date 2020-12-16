def randomname():
    import json
    import random
    with open('namedatabase.json') as json_file:
        data = json.load(json_file)

        names = []
        limit = 0
    
        for p in data['results']:
            names.append(p['Name'])
            limit += 1
            #print('Name: ' + p['Name'])
            #print('Website: ' + p['website'])
            #print('From: ' + p['from'])
            #print('')

        name = names[random.randint(0,limit)]
        #print(name)
        return name


'''def randomname():
    name = "John"
    return name'''
