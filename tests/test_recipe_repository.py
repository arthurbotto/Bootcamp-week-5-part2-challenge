from lib.recipe import *
from lib.recipe_repository import *

def test_get_all_recipes(db_connection): 
    db_connection.seed("seeds/recipes.sql") 
    repository = RecipeRepository(db_connection)

    recipes = repository.all() 
    print(recipes)

   
    assert recipes == [
        Recipe(1, 'Spaghetti Carbonara', 20, 4),
        Recipe(2, 'Chicken Yakisoba', 15, 4.5),
        Recipe(3, 'Pepperoni Pizza', 25, 4.9),
        Recipe(4, 'Banana Split', 10, 5),
        Recipe(5, 'Kakuni Ramen', 30, 4.3)
    ]

def test_find_recipe_by_id(db_connection):
    db_connection.seed("seeds/recipes.sql") 
    repository = RecipeRepository(db_connection)

    recipe = repository.find(1, 'id')
    assert recipe == Recipe(1, 'Spaghetti Carbonara', 20, 4)

def test_find_recipe_by_rating(db_connection):
    db_connection.seed("seeds/recipes.sql") 
    repository = RecipeRepository(db_connection)

    recipe = repository.find(5, 'rating')
    assert recipe == Recipe(4, 'Banana Split', 10, 5)