from collections import defaultdict


class City:
    def __init__(self, name: str, department: int, country: str, population: int):
        self.name = name
        self.department = department
        self.population = population
        self.country = country

    def __str__(self):
        return f"City: {self.name} has {self.population} inhabitants and is located in {self.department}, {self.country}"

    def __repr__(self):
        return str(self)


class Db:
    def __init__(self, db: list[City]):
        self.cities: dict[str, City] = {city.name: city for city in db}
        self.department_index = dict()
        self.__update_index()
        print("Successfully loaded ", len(db), "cities")

    def add(self, city: City):
        self.cities[city.name] = city
        self.__update_index()

    def delete(self, city_name: str):
        del self.cities[city_name]
        self.__update_index()

    def list_in_department(self, department: int) -> list[City]:
        return self.department_index[department]

    def __getitem__(self, city_name: str):
        return self.cities[city_name]

    def __update_index(self):
        self.department_index = defaultdict(list)
        for city in self.cities.values():
            self.department_index[city.department].append(city)

    def flush(self, path: str):
        with open(path, "wt+") as fp:
            for city in self.cities.values():
                fp.write(f"{city.name},{city.department},{city.country},{city.population}\n")

        print(f"Successfully wrote {len(self.cities)} in {path}")
