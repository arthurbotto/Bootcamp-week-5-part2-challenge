from lib.database_connection import DatabaseConnection
from lib.recipe import *
from lib.recipe_repository import *


connection = DatabaseConnection()
connection.connect()


connection.seed("seeds/recipes.sql")

recipe_repo = RecipeRepository(connection)
result = recipe_repo.all()
for recipe in result:
    print(recipe)

result2 = recipe_repo.find(5, 'rating')
print(result2)