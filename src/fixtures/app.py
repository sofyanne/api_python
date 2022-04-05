import src.repository.recipe as recipe_repository
import src.repository.ingredient as ingredient_repository

def load_recipes():
    recipes = [
        {
            'title': 'Pizza 6 fromages'
        },
        {
            'title': 'Pizza bolo'
        },
        {
            'title': 'Pizz à poil'
        },
        {
            'title': 'Pizza kebab'
        },
        {
            'title': 'Pizza Margarita'
        },
        {
            'title': 'Pizza Reine'
        },
    ]
    
    for recipe in recipes:
        recipe_repository.create_new_recipe(recipe)

def load_ingredients():
    ingredients = [
        {
            'labem': 'Cheddar'
        },
        {
            'labem': 'Emmental'
        },
        {
            'labem': 'Poulet'
        },
        {
            'labem': 'Viande hachée'
        },
        {
            'labem': 'Tomate'
        },
        {
            'labem': 'Champignons'
        },
    ]
    
    for ingredient in ingredients:
        ingredient_repository.create_new_ingredient(ingredient)
