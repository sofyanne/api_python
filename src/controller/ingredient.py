import src.repository.ingredient as ingredient_repository
import json


def index():
    # Récuperer toutes les recette en BDD
    ingredients = ingredient_repository.get_all_ingredients()
    # Afficher les recettes à l'utilisateur
    print(json.dumps(ingredients))


def show():
    return ingredient_repository.get_all_ingredients()


def new():
    pass


def edit():
    pass


def delete():
    pass
