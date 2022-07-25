import json

class dog_class():
    
    def dogindex(index: int):
        jfile = open("./dogslist/labels.json","r")
        dog_list = json.load(jfile)
            
        return dog_list['razas'][index][str(index+1)]