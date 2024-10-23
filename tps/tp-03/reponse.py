from abc import ABC, abstractmethod
import math
"""
Créez une classe abstraite Shape avec une méthode abstraite area().
Implémentez deux classes dérivées : 
Circle et Rectangle.
Chaque classe devra implémenter sa propre version de la méthode area().
"""

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    """
    :param radius: float

    :return float : area of the circle
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
       return  math.pi * self.radius ** 2


class Rectangle(Shape):

        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height


class BankAccount():
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, amount):
        self.balance += amount
        return self

    def __sub__(self, amount):
        self.balance -= amount
        return self


def check_positive(func):
    def wrapper(num):
        if num < 0:
            raise ValueError()
        return func(num)
    return wrapper


class Car():
    def __init__(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value <= 0 or value >= 200:
            raise ValueError("Vitesse invalide")
        self._speed = value


class AgeError(Exception):
    pass
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0 or value >= 150:
            raise AgeError("Age invalide")
        self._age = value


"""
Implémentez un pattern Singleton pour une classe DatabaseConnection qui garantit qu’il n’existe qu’une seule instance de connexion à la base de données.

L'instance de cette classe doit permettre de créer un context (qui, lui, n'est pas unique), et qui permet d'ajouter une entrée (id, data), de la supprimer par id, ou de drop toutes les lignes.
Les opérations doivent être exécutées (flush) une fois le context fermé.
"""
class DatabaseConnection():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.entries = []
        return cls._instance

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_by_id(self, id):
        self.entries = [entry for entry in self.entries if entry["id"] != id]

    def drop_all(self):
        self.entries = []

class DbContext():
    def __init__(self, db):
        self.db = db

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def add_entry(self, entry):
        self.db.add_entry(entry)

    def remove_by_id(self, id):
        self.db.remove_by_id(id)

    def drop_all(self):
        self.db.drop_all()

class ShapeFactory():
    @staticmethod
    def create(shape, **kwargs):
        if shape == "circle":
            return Circle(kwargs["radius"])
        elif shape == "rectangle":
            return Rectangle(kwargs["width"], kwargs["height"])
        else:
            return None

import threading
import time

# Exception personnalisée si nécessaire
class TimeoutError(Exception):
    pass

# Création du décorateur timeout_limit
def timeout_limit(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Fonction interne pour exécuter la fonction dans un thread
            result = [None]  # Liste mutable pour stocker le résultat
            exception = [None]  # Liste mutable pour stocker une éventuelle exception

            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exception[0] = e

            # Lancement de la fonction dans un thread
            thread = threading.Thread(target=target)
            thread.start()

            # On attend que le thread finisse ou dépasse la limite de temps
            thread.join(timeout=seconds)

            # Si le thread est encore actif après le timeout, lever TimeoutError
            if thread.is_alive():
                raise TimeoutError(f"Fonction a pris plus de {seconds} secondes à s'exécuter")

            # Si une exception a été levée dans le thread, on la relance ici
            if exception[0]:
                raise exception[0]

            return result[0]
        return wrapper
    return decorator

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)



class Matrix():
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        return Matrix([[self.values[i][j] + other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))])

    def __sub__(self, other):
        return Matrix([[self.values[i][j] - other.values[i][j] for j in range(len(self.values[0]))] for i in range(len(self.values))])
    def __mul__(self, other):
        return Matrix([[sum([self.values[i][k] * other.values[k][j] for k in range(len(self.values[0]))]) for j in range(len(other.values[0]))] for i in range(len(self.values))])


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof"


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Meow"

class AnimalFactory():
    @staticmethod
    def create(animal_type, name):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            return None

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ne__(self, other):
        return self.price != other.price

class Account():
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._balance = value

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Le montant du dépôt ne peut pas être négatif")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Le montant du retrait ne peut pas être négatif")
        if amount > self.balance:
            raise ValueError("Le montant du retrait dépasse le solde")
        self.balance -= amount

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


class Mock:
    def __init__(self, original_function, return_value):
        self.original_function = original_function
        self.return_value = return_value

    def __enter__(self):
        self.original_function = self.original_function.__get__(self)
        self.original_function.__globals__[self.original_function.__name__] = self

    def __exit__(self, type, value, traceback):
        self.original_function.__globals__[self.original_function.__name__] = self.original_function

    def __call__(self, *args, **kwargs):
        return self.return_value

class Statistics:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    def mode(self):
        counts = {}
        for value in self.data:
            if value in counts:
                counts[value] += 1
            else:
                counts[value] = 1
        max_count = max(counts.values())
        return [key for key, value in counts.items() if value == max_count]

    def std_dev(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return math.sqrt(variance)

class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

class stats():
    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            return sorted_data[n // 2]

    @staticmethod
    def variance(data):
        mean = stats.mean(data)
        return sum((x - mean) ** 2 for x in data) / len(data)