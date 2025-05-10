



import random
import json

PATH_PREDMETI= "C:/Users/ilush/PycharmProjects/pythonProject/fle/rpg_game/json/predmeti.json"
PATH_IGROKI= "C:/Users/ilush/PycharmProjects/pythonProject/fle/rpg_game/json/igroki.json"

def load_igroki():
    try:
        with open(PATH_IGROKI, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_igroki(data):
    with open(PATH_IGROKI, "w",encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False, indent=4)

def get_predmeti():
    try:
        with open(PATH_PREDMETI, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return {}

def get_predmet_by_id(id_predmet):
    try:
        with open(PATH_PREDMETI, "r", encoding="utf-8") as file:
            data=json.load(file)
            return data.get(id_predmet)
    except:
        return {}

def set_predmet_to_igrok(id_predmet, id_igroki):
    predmet=get_predmet_by_id(id_predmet)
    data=load_igroki()
    igrok=data.get(id_igroki)
    if igrok.get("inventar")==None:
        igrok["inventar"]={}

    if igrok["inventar"].get(id_predmet):
        igrok["inventar"][id_predmet]["kolvo"]+=1
    else:
        igrok["inventar"][id_predmet]=predmet

    data[id_igroki]=igrok
    save_igroki(data)

def delet_predmet_to_igrok(id_predmet,id_igroki):
    predmet=get_predmet_by_id(id_predmet)
    data=load_igroki()
    igrok=data.get(id_igroki)

    if igrok["inventar"].get(id_predmet):
        igrok["inventar"][id_predmet]["kolvo"]-=1
        if igrok["inventar"][id_predmet]["kolvo"]==0:
            del igrok["inventar"][id_predmet]

    data[id_igroki]=igrok
    save_igroki(data)

def get_choice_random_id_predmet(procent):
    if random.randint(1,100)<procent:
        predmeti=get_predmeti()
        predmet=random.choice(list(predmeti))
        return predmet
    else:
        return None

def get_inventar(id_igrok):
    inventar=load_igroki().get(id_igrok).get("inventar")
    return inventar

if __name__=="__main__":
    print(get_predmeti())
    print(get_predmet_by_id("kamen1"))
    print(set_predmet_to_igrok("kamen1","000000000"))
    #print(delet_predmet_to_igrok("kamen1","000000000"))
    print(get_inventar("000000000"))
    print(get_choice_random_id_predmet(33))