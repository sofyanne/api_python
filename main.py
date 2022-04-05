import src.controller.recipe as recipe_controller
import src.controller.ingredient as ingredient_controller
import src.fixtures.app as fixtures
import sys

args = sys.argv
call = args[1] if len(args) > 1 else None

commands = {
    "load:fixtures": fixtures.load_ingredients
 
}

if call and call in commands:
    commands.get(call)()
    exit()

routes = {
    "/api/recipes/": recipe_controller.index,
    "/api/ingredients/": ingredient_controller.index
}

if call and call in routes:
    routes.get(call)()
    exit()

print("Not found - 404")
