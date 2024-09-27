# **Cours Python EPSI**

---

# **Cours 2 : Programmation Orientée Objet Avancée et Exceptions**

## Objectifs

Dans ce cours, nous allons approfondir la Programmation Orientée Objet (POO) en abordant des concepts clés comme l'héritage, le polymorphisme, la gestion des exceptions, la création d'exceptions personnalisées, le pattern matching, le mot-clé `with`, les classes auto-fermetures, et les générateurs.

---

## Héritage et Polymorphisme

### Héritage

L'héritage permet à une classe d'hériter des attributs et méthodes d'une autre classe, appelée classe parente ou super-classe. Cela permet de réutiliser le code et de le spécialiser pour créer de nouvelles fonctionnalités.

**Exemple d'héritage en Python :**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} fait du bruit."


class Dog(Animal):
    def speak(self):
        return f"{self.name} aboie."


class Cat(Animal):
    def speak(self):
        return f"{self.name} miaule."


# Utilisation des classes
dog = Dog("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Rex aboie.
print(cat.speak())  # Whiskers miaule.
```

### Polymorphisme

Le polymorphisme permet à des objets de classes différentes de répondre à la même méthode d'une manière spécifique à leur type. Cela rend le code plus flexible et extensible.

**Exemple de polymorphisme en Python :**

```python
def make_animal_speak(animal):
    print(animal.speak())


dog = Dog("Rex")
cat = Cat("Whiskers")

make_animal_speak(dog)  # Rex aboie.
make_animal_speak(cat)  # Whiskers miaule.
```

---

## Gestion des Exceptions

### Bloc `try/except`

Le bloc `try` capture les exceptions potentielles, et le bloc `except` gère les erreurs rencontrées.

**Exemple :**

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erreur : division par zéro.")
```

### Bloc `finally`

Le bloc `finally` s'exécute toujours, que l'exception soit levée ou non, et est utilisé pour les opérations de nettoyage.

**Exemple :**

```python
try:
    file = open("example.txt", "r")
finally:
    file.close()
```

---

## Création d'Exceptions Personnalisées

En Python, vous pouvez créer vos propres exceptions en héritant de la classe `Exception` (ou d'une de ses sous classes). Cela permet de définir des erreurs spécifiques à votre application et de mieux gérer les cas d'erreur.

### Exemple de création d'une exception personnalisée :

```python
class InvalidAgeError(Exception):
    def __init__(self, age, message="L'âge doit être compris entre 0 et 120."):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.age} -> {self.message}"


def check_age(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    print(f"L'âge {age} est valide.")


try:
    check_age(150)
except InvalidAgeError as e:
    print(e)
```

---

## Pattern Matching (Python 3.10+)

Le **pattern matching** a été ajouté sous la forme d'une instruction match et d'instructions case pour les motifs avec des actions associées. Les motifs filtrent des séquences, des dictionnaires, des types de données et des instances de classes. Le filtrage par motifs permet aux programmes d'extraire de l'information de types de données complexes, faire du branchement selon la structure des données et réaliser des actions spécifiques en fonction des différentes formes des données.

### Exemple basique :

```python
def describe_point(point):
    match point:
        case (0, 0):
            return "Origine"
        case (0, y):
            return f"Axe Y, à {y}"
        case (x, 0):
            return f"Axe X, à {x}"
        case (x, y):
            return f"Point quelconque à ({x}, {y})"
        case _:
            return "C'est autre chose"


print(describe_point((0, 0)))  # Origine
print(describe_point((0, 3)))  # Axe Y, à 3
print(describe_point((2, 0)))  # Axe X, à 2
print(describe_point((2, 3)))  # Point quelconque à (2, 3)
```

### Pattern Matching avec des Classes :

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def process_point(point):
    match point:
        case Point(x=0, y=0):
            return "Origine"
        case Point(x=0, y=y):
            return f"Sur l'axe Y à {y}"
        case Point(x=x, y=0):
            return f"Sur l'axe X à {x}"
        case Point(x=x, y=y):
            return f"Point à ({x}, {y})"


point = Point(0, 5)
print(process_point(point))  # Sur l'axe Y à 5
```

---

## Mot-clé `with` et Classes Auto-Fermetures

### Utilisation du Mot-clé `with`

Le mot-clé `with` simplifie la gestion des ressources en assurant leur nettoyage automatique. Il est souvent utilisé pour la gestion des fichiers, des connexions, etc.

**Exemple avec la gestion de fichiers :**

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

Dans cet exemple, le fichier est automatiquement fermé après la fin du bloc `with`, même en cas d'erreur.

### Création de Classes Auto-Fermetures

Pour créer des classes qui se ferment automatiquement, vous devez implémenter les méthodes `__enter__` et `__exit__`. Cela rend la classe compatible avec le mot-clé `with`.

**Exemple de classe auto-fermeture :**

```python
class Resource:
    def __enter__(self):
        print("Acquisition de la ressource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Libération de la ressource")

    def do_something(self):
        print("Utilisation de la ressource")


with Resource() as resource:
    resource.do_something()
```

---

## Générateurs et `yield`

Les générateurs sont des fonctions qui produisent une séquence de valeurs à l'aide du mot-clé `yield`. Ils permettent de générer des éléments un par un et de conserver leur état entre les appels.

### Exemple de générateur :

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)
```

Dans cet exemple, la fonction `count_up_to` génère des nombres de 1 à `max`. Chaque appel à `yield` renvoie une valeur et suspend l'exécution de la fonction jusqu'au prochain appel.

### Avantages des Générateurs

- **Faible empreinte en mémoire** : Ils permettent de travailler avec de grandes séquences de données sans les charger entièrement en mémoire.
- **Lazy Evaluation** : Les valeurs sont générées à la demande.

---

## Travaux Pratiques (TD)

### Exercice : Gestion d'une Bibliothèque

Développer un système de gestion de bibliothèque avec des classes pour les **livres**, les **auteurs**, et une **bibliothèque**.

1. **Classe `Livre`** : Attributs `titre`, `auteur`, `année`.
2. **Classe `Auteur`** : Attributs `nom`, `date_naissance`.
3. **Classe `Bibliothèque`** : Méthodes pour ajouter des livres, rechercher des livres par auteur, etc.
4. Implémenter une fonctionnalité pour sauvegarder l'état de la bibliothèque dans un fichier et pour le charger depuis ce fichier.

---

## Ressources Complémentaires

- Documentation officielle de Python : [https://docs.python.org/fr/3/tutorial/index.html](https://docs.python.org/fr/3/tutorial/index.html)
- Tutoriel POO Python : [https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp)
- Générateurs : [https://docs.python.org/3/howto/pyworking.html#generators](https://docs.python.org/3/howto/pyworking.html#generators)
- Pattern Matching : [https://docs.python.org/3/whatsnew/3.10.html#new-syntax-features](https://docs.python.org/3/whatsnew/3.10.html#new-syntax-features)

---

**Fin du Cours 2**
