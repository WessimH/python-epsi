from db import City, Db

cities = []

with open("./input.csv") as fp:
    for line in fp:
        name, department_as_str, country, population_as_str = line.split(",")
        cities.append(City(name, int(department_as_str), country, int(population_as_str)))

db = Db(cities)


def process_prompt(prompt: str) -> bool:
    prompt_split = prompt.split(" ")
    if prompt.startswith("get city"):
        _, _, city = prompt_split
        print(db[city])
        return True
    elif prompt.startswith("get department"):
        _, _, department_as_str = prompt_split
        print(db.list_in_department(int(department_as_str)))
        return True
    elif prompt.startswith("add "):
        _, city_name, department_as_str, country, population_as_str = prompt_split
        city = City(city_name, int(department_as_str), country, int(population_as_str))
        db.add(city)
        print("Added", city)
        return True
    elif prompt.startswith("delete"):
        _, city_name = prompt_split
        db.delete(city_name)
        print(city_name, "was deleted")
        return True
    elif prompt == "flush":
        db.flush("./input.csv")
        return True
    return False

process_prompt("add Vertou 44 France 10000")
process_prompt("flush")
process_prompt("get city Vertou")

while process_prompt(input()):
    pass
