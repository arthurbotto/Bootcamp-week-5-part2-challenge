from lib.recipe import *

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes = []
        
        for row in rows:
            recipe = Recipe(row["id"], row["name"], row["time"], row["rating"])
            recipes.append(recipe)
        print(recipes)
        return recipes
    
    def find(self, parameter, column):
        rows = self._connection.execute(f'SELECT * FROM recipes WHERE {column} = %s', [parameter])
        dish = []
        for row in rows:
            recipe = Recipe(row["id"], row["name"], row["time"], row["rating"])
            dish.append(recipe)

        return dish[0]