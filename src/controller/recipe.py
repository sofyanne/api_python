import src.repository.recipe as recipe_repository
from src.entity.Recipe import Recipe

def index():
    # Récuperer toutes les recette en BDD
    recipes = recipe_repository.get_all()
    # Afficher les recettes à l'utilisateur
    for recipe in recipes:
        print(recipe)

def show(id: int):
    print(f"Récupération de la recette d'id {id}")

def new():
    id = recipe_repository.create(Recipe(None, "Pizza chorizo"))


def edit():
    pass

def delete():
    pass