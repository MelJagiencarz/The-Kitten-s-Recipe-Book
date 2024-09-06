import pytest
from unittest.mock import patch

from project import add_recipe
from project import search_recipe
from project import generate_list
from project import edit_recipe
from project import delete_recipe

def test_add_recipe():
    recipes = []

    user_inputs = ['Brownies',
                   'sugar, butter, eggs, cocoa powder, flour, vanilla extract, baking powder, salt',
                   'Mix all ingredients and bake at 350°F for 25-30 minutes.'
    ]
    with patch('builtins.input', side_effect=user_inputs):
        add_recipe(recipes)

    assert len(recipes) == 1
    assert recipes[0]['name'] == 'Brownies'
    assert recipes[0]['ingredients'] == ['sugar', 'butter', 'eggs', 'cocoa powder', 'flour', 'vanilla extract', 'baking powder', 'salt']
    assert recipes[0]['instructions'] == 'Mix all ingredients and bake at 350°F for 25-30 minutes.'


    user_inputs2 = ['Pancakes',
                    'flour, sugar, baking powder, salt, milk, egg, butter, vanilla extract',
                    'In a large bowl, mix the flour, sugar, baking powder, and salt. In another bowl, whisk the milk, egg, melted butter, and vanilla extract. Pour the wet ingredients into the dry ingredients and stir until combined. Heat a non-stick pan over medium heat and pour 1/4 cup of batter for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown.'
    ]
    with patch('builtins.input', side_effect=user_inputs2):
        add_recipe(recipes)

    assert len(recipes) == 2
    assert recipes[1]['name'] == 'Pancakes'
    assert recipes[1]['ingredients'] == ['flour', 'sugar', 'baking powder', 'salt', 'milk', 'egg', 'butter', 'vanilla extract']
    assert recipes[1]['instructions'] == 'In a large bowl, mix the flour, sugar, baking powder, and salt. In another bowl, whisk the milk, egg, melted butter, and vanilla extract. Pour the wet ingredients into the dry ingredients and stir until combined. Heat a non-stick pan over medium heat and pour 1/4 cup of batter for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown.'


def test_search_recipe():
    recipes = [
        {
        'name': 'Brownies',
        'ingredients': ['sugar', 'butter', 'eggs', 'cocoa powder', 'flour', 'vanilla extract', 'baking powder', 'salt'],
        'instructions': 'Mix all ingredients and bake at 350°F for 25-30 minutes.'
        },
        {
        'name': 'Pancakes',
        'ingredients': ['flour', 'sugar', 'baking powder', 'salt', 'milk', 'egg', 'butter', 'vanilla extract'],
        'instructions': 'In a large bowl, mix the flour, sugar, baking powder, and salt. In another bowl, whisk the milk, egg, melted butter, and vanilla extract. Pour the wet ingredients into the dry ingredients and stir until combined. Heat a non-stick pan over medium heat and pour 1/4 cup of batter for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown.'
        },
        {
        'name': 'Caesar Salad',
        'ingredients': ['romaine lettuce', 'croutons', 'parmesan cheese', 'Caesar dressing', 'lemon juice', 'olive oil', 'garlic', 'anchovy paste', 'black pepper'],
        'instructions': 'In a large bowl, toss the romaine lettuce with croutons, parmesan cheese, and Caesar dressing. In a separate bowl, mix lemon juice, olive oil, garlic, and anchovy paste, then drizzle over the salad. Season with black pepper and toss again.'
        }
    ]

    def test_found_recipe():
        user_input = ['caesar Salad']
        with patch('builtins.input', side_effect=user_input):
            result = search_recipe(recipes)
        assert result == True

    def test_not_found_recipe():
        user_input = ['French Fries']
        with patch('builtins.input', side_effect=user_input):
            result = search_recipe(recipes)
        assert result == False


def test_generate_list():
    recipes = [
        {
        'name': 'Brownies',
        'ingredients': ['sugar', 'butter', 'egg', 'egg', 'cocoa powder', 'flour', 'vanilla extract', 'baking powder', 'salt'],
        'instructions': 'Mix all ingredients and bake at 350°F for 25-30 minutes.'
        },
        {
        'name': 'Pancakes',
        'ingredients': ['flour', 'sugar', 'baking powder', 'salt', 'milk', 'egg', 'butter', 'vanilla extract'],
        'instructions': 'In a large bowl, mix the flour, sugar, baking powder, and salt. In another bowl, whisk the milk, egg, melted butter, and vanilla extract. Pour the wet ingredients into the dry ingredients and stir until combined. Heat a non-stick pan over medium heat and pour 1/4 cup of batter for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown.'
        }
     ]
    expected_shopping_list = {
        'sugar': 2,
        'butter': 2,
        'egg': 3,
        'cocoa powder': 1,
        'flour': 2,
        'vanilla extract': 2,
        'baking powder': 2,
        'salt': 2,
        'milk': 1,
    }

    shopping_list, _ = generate_list(recipes)
    assert shopping_list == expected_shopping_list


def test_edit_recipe():
    recipes = [
        {
        'name': 'Brownies',
        'ingredients': ['sugar', 'butter', 'egg', 'egg', 'cocoa powder', 'flour', 'vanilla extract', 'baking powder', 'salt'],
        'instructions': 'Mix all ingredients and bake at 350°F for 25-30 minutes.'
        },
        {
        'name': 'Pancakes',
        'ingredients': ['flour', 'sugar', 'baking powder', 'salt', 'milk', 'egg', 'butter', 'vanilla extract'],
        'instructions': 'In a large bowl, mix the flour, sugar, baking powder, and salt. In another bowl, whisk the milk, egg, melted butter, and vanilla extract. Pour the wet ingredients into the dry ingredients and stir until combined. Heat a non-stick pan over medium heat and pour 1/4 cup of batter for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown.'
        }
     ]

    def test_edit_name():
        user_input = ['pancakes', 'name', 'Golden Pancakes']
        with patch('builtins.input', side_effect=user_input):
            edit_recipe(recipes)
        assert recipes[1]['name'] == 'Golden Pancakes'

    def test_edit_ingredients():
        user_input = ['Pancakes', 'ingredients', 'oatmeal, egg, honey, milk']
        with patch('builtins.input', side_effect=user_input):
            edit_recipe(recipes)
        assert recipes[1]['ingredients'] == ['oatmeal', 'egg', 'honey', 'milk']

    def test_edit_instructions():
        user_input = ['Pancakes', 'instructions', 'Just mix everything together and cook them on a pan']
        with patch('builtins.input', side_effect=user_input):
            edit_recipe(recipes)
        assert recipes[1]['instructions'] == 'Just mix everything together and cook them on a pan'

def test_delete_recipe(monkeypatch):
    recipes = [
        {
        'name': 'Brownies',
        'ingredients': ['sugar', 'butter', 'egg', 'egg', 'cocoa powder', 'flour', 'vanilla extract', 'baking powder', 'salt'],
        'instructions': 'Mix all ingredients and bake at 350°F for 25-30 minutes.'
        },
        {
        'name': 'Pancakes',
        'ingredients': ['flour', 'sugar', 'baking powder', 'salt', 'milk', 'egg', 'butter', 'vanilla extract'],
        'instructions': 'In a large bowl, mix the flour, sugar, baking powder, and salt. In another bowl, whisk the milk, egg, melted butter, and vanilla extract. Pour the wet ingredients into the dry ingredients and stir until combined. Heat a non-stick pan over medium heat and pour 1/4 cup of batter for each pancake. Cook until bubbles form on the surface, then flip and cook until golden brown.'
        }
     ]

    monkeypatch.setattr('builtins.input', lambda _: 'Brownies')
    delete_recipe(recipes)

    assert len(recipes) == 1
    assert recipes[0]['name'] == 'Pancakes'
