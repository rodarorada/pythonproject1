


sl={
    "0001":{
        "name":"Петр",
        "age": 47,
        "children": ["0003","0004"],
        "parents": []
    },
    "0002": {
        "name": "Alisa",
        "age": 43,
        "children": ["0003","0004"],
        "parents": []
    },
    "0003": {
            "name": "Andrey",
            "age": 16,
            "children": [],
            "parents": ["0001", "0002"]
        },
    "0004": {
            "name": "Sonya",
            "age": 13,
            "children": [],
            "parents": ["0001", "0002"]
            }
}

def children(id):
    chiren=sl.get(id).get("children")
    # print(chiren)
    for children_id in chiren:
        # print(children_id)
        children_name=sl.get(children_id).get("name")
        print(children_name)


children("0001")

def parents(id):
    parentss = sl.get(id).get("parents")
    name = sl.get(id).get("name")
    st=f"у {name} родители - "
    # print(parentss)
    if len(parentss)>0:
        for parents_id in parentss:
            parents_age = sl.get(parents_id).get("age")
            # print(parents_id)
            parents_name = sl.get(parents_id).get("name")
            st+=parents_name
            st = st + " " + str(parents_age) + " лет "
        print(st + ".")
    else:
        print("родителей нет.")

parents("0001")

def B_S(id):
    name = sl.get(id).get("name")
    parents=sl.get(id).get("parents")
    if len(parents)==0:
        print("братьев и сестёр нет.")
        return
    parent = parents[0]
    st=f"у {name} есть братья и сёстры - "
    parent_children = sl.get(parent).get("children")

    if len(parent_children)>1:
        for childdren in parent_children:
            if childdren != id:
                childdren_name = sl.get(childdren).get("name")
                st = st + childdren_name + ", "
        print(st + ".")

B_S("0001")