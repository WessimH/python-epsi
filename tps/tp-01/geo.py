from db import City, Db

cities = []

with open("./input.csv", "r") as fp:
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
        _, city_or_dep, department_as_str, country, population_as_str = prompt_split
        city = City(city_or_dep, int(department_as_str), country, int(population_as_str))
        db.add(city)
        print("Added", city)
        return True
    elif prompt.startswith("delete"):
        _, city_or_dep = prompt_split
        db.delete(city_or_dep)
        print(city_or_dep, "was deleted")
        return True
    elif prompt == "flush":
        db.flush("./input.csv")
        return True
    elif prompt.startswith("top "):
        pass
    return False














print(db.top(10))