
# **Cours 3 : Programmation Orientée Objet Avancée en Python (Classes Abstraites, Surcharge d’Opérateurs, Design Patterns)**

## **Objectifs du Cours :**
- Comprendre et utiliser les **classes abstraites** pour structurer leur code.
- Surcharger des **opérateurs** et des **méthodes** pour adapter le comportement des objets.
- Mettre en œuvre des **design patterns** classiques, tels que le **pattern Factory**, dans un contexte de POO avancée.

---

### **1. Classes Abstraites en Python**

Les **classes abstraites** sont des classes qui ne peuvent pas être instanciées directement et qui contiennent des méthodes que les classes dérivées doivent implémenter. En Python, elles sont définies à l'aide du module `abc` (Abstract Base Classes).

#### **Exemple :**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return f"{self.name} aboie."

class Cat(Animal):
    def sound(self):
        return f"{self.name} miaule."

# Utilisation
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.sound())  # Rex aboie.
print(cat.sound())  # Whiskers miaule.
```

- **Explication** : La classe `Animal` est abstraite et ne peut pas être instanciée directement. Elle oblige les classes `Dog` et `Cat` à implémenter la méthode `sound()`.

---

### **2. Surcharge d'Opérateurs**

Python permet de **surcharger des opérateurs** en définissant des méthodes spéciales (méthodes magiques) comme `__add__`, `__sub__`, `__eq__`, etc., pour permettre aux objets d’interagir avec les opérateurs de manière personnalisée.

#### **Exemple de surcharge de l’opérateur `+` :**

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Surcharge de l'opérateur +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Utilisation
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2  # Appelle __add__
print(v3)  # Vector(4, 6)
```

- **Explication** : La méthode `__add__` est utilisée pour définir ce que signifie l’opérateur `+` pour la classe `Vector`.

#### **Autre exemple avec `__eq__` :**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

# Utilisation
p1 = Person("Alice", 30)
p2 = Person("Alice", 30)
p3 = Person("Bob", 25)

print(p1 == p2)  # True
print(p1 == p3)  # False
```

- **Explication** : Ici, l'opérateur `==` compare les objets `Person` en fonction de leurs attributs `name` et `age`.

---

### **3. Surcharge de Méthodes**

La **surcharge de méthodes** permet de redéfinir une méthode d’une classe parent dans une classe dérivée. En Python, cela se fait en réécrivant la méthode dans la classe fille tout en conservant la possibilité d'appeler la méthode de la classe parent via `super()`.

#### **Exemple :**

```python
class Animal:
    def speak(self):
        return "Un animal fait du bruit."

class Dog(Animal):
    def speak(self):
        return "Le chien aboie."

# Utilisation
animal = Animal()
dog = Dog()

print(animal.speak())  # Un animal fait du bruit.
print(dog.speak())  # Le chien aboie.
```

- **Explication** : La méthode `speak` est surchargée dans la classe `Dog`.

---

### **4. Design Pattern - Factory**

Le **pattern Factory** permet de déléguer la création d'objets à une méthode dédiée, en masquant la logique de création derrière une interface commune. Cela permet de créer des objets dynamiquement en fonction des besoins, sans connaître les détails de leur instanciation.

#### **Exemple :**

```python
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        match animal_type:
            case "dog":
                return Dog()
            case "cat":
                return Cat()
            case _:
                return None

# Utilisation
animal = AnimalFactory.get_animal("dog")
print(animal.speak())  # Woof!
```

- **Explication** : La factory `AnimalFactory` permet de créer un objet `Dog` ou `Cat` en fonction d’une chaîne de caractères. L'opérateur `match` permet de gérer dynamiquement la création des instances.

---

### **5. Exemple Avancé : Système de Gestion d'une Pizzeria**

Dans cet exemple, nous allons intégrer plusieurs concepts avancés de POO, notamment :
- Les **classes abstraites** pour structurer le système de commande.
- La **surcharge de méthodes** pour gérer les différentes types de pizzas et boissons.
- Un **design pattern Factory** pour générer des commandes dynamiquement.

#### **Étape 1 : Définition des classes abstraites et surcharges**

```python
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_price(self):
        pass

class Pizza(Product):
    def __init__(self, name, price, toppings=[]):
        super().__init__(name, price)
        self.toppings = toppings

    def get_price(self):
        return self.price + len(self.toppings) * 0.5  # Prix supplémentaire par garniture

class Drink(Product):
    def get_price(self):
        return self.price
```

#### **Étape 2 : Implémentation de la Factory avec `match`**

```python
class ProductFactory:
    @staticmethod
    def create_product(product_type, name, price, *args):
        match product_type:
            case "pizza":
                return Pizza(name, price, args)
            case "drink":
                return Drink(name, price)
            case _:
                raise ValueError(f"Type de produit inconnu : {product_type}")

# Utilisation
pizza = ProductFactory.create_product("pizza", "Margherita", 8.5, "tomate", "mozzarella")
drink = ProductFactory.create_product("drink", "Coca", 2.0)

print(pizza.get_price())  # Prix calculé avec les garnitures
print(drink.get_price())  # Prix fixe pour la boisson
```

---
