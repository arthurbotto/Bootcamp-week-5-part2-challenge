from lib.recipe import *

def test_recipe_constructs():
    recipe = Recipe(1, "Kakuni Ramen", 30, 4.3)
    assert recipe.id == 1
    assert recipe.name == "Kakuni Ramen"
    assert recipe.time == 30
    assert recipe.rating == 4.3

def test_recipe_format_nicely():
    recipe = Recipe(1, "Kakuni Ramen", 30, 4.3)
    assert str(recipe) == "Recipe(1, Kakuni Ramen, 30, 4.3)"

def test_albums_are_equal():
    recipe1 = Recipe(1, "Kakuni Ramen", 30, 4.3)
    recipe2 = Recipe(1, "Kakuni Ramen", 30, 4.3)
    assert recipe1 == recipe2