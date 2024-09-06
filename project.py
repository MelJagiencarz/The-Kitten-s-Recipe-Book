import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

def main():
    recipes = []
    print("Welcome to our Recipe Manager!")
    while True:
        print("0. See your recipes book")
        print("1. Add recipe")
        print("2. Search recipe")
        print("3. Generate shooping list")
        print("4. Edit recipe")
        print("5. Delete recipe")
        print("6. Exit")

        choice = input("Choose an option's number: ")

        if choice == '0':
            for recipe in recipes:
                console.print(Panel(show_recipe(recipe), border_style="magenta", title_align="left"))
        elif choice == '1':
            add_recipe(recipes)
        elif choice == '2':
            search_recipe(recipes)
        elif choice == '3':
            shopping_list, table = generate_list(recipes)
            console.print(table)
        elif choice == '4':
            edit_recipe(recipes)
        elif choice == '5':
            delete_recipe(recipes)
        elif choice == '6':
            sys.exit('Thank you for using our recipe manager!')
        else:
            print("Invalid choice, please type a valid option's number")

def show_recipe(recipe):
    title = Text(recipe["name"], style="bold cyan underline")

    ingredients_title = Text("\nIngredients:\n", style="bold green")
    ingredients_list = "\n".join(f"☆ {ingredient}" for ingredient in recipe["ingredients"])

    instructions_title = Text("\nInstructions\n", style="bold yellow")
    instructions = Text(recipe["instructions"], style="dim white")

    recipe_text = title + ingredients_title + Text(ingredients_list, style="dim white") +instructions_title + instructions
    return recipe_text

def add_recipe(recipes):
    name = input("Enter recipe's name: ")
    ingredients = input("Enter recipe's ingredients (comma-separated): ").split(',')
    instructions = input("Enter recipe's instructions: ")

    new_recipe = {
        'name': name.strip(),
        'ingredients': [ingredient.strip() for ingredient in ingredients],
        'instructions': instructions.strip()
    }

    recipes.append(new_recipe)
    print(f"{name}'s recipe has been added succesfully!")


def search_recipe(recipes):
    name = input("Which is the recipe's name? ")

    for recipe in recipes:
        if recipe['name'].lower() == name.lower():
            console.print(Panel(show_recipe(recipe), border_style="magenta", title_align="left"))
            return True

    print("The recipe couldn't be found, are you sure you have already added it to the recipes book?")
    return False

def generate_list(recipes):
    shopping_list = {}

    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            if ingredient in shopping_list:
                shopping_list[ingredient] += 1
            else:
                shopping_list[ingredient] = 1

    table = Table(title="Shopping List")
    table.add_column("Ingredient", style="cyan")
    table.add_column("Quantity", style="magenta")

    for ingredient, quantity in shopping_list.items():
        table.add_row(ingredient, str(quantity))

    return shopping_list, table


def edit_recipe(recipes):
    name = input("Which is the name of the recipe you want to edit? ")

    for recipe in recipes:
        if recipe['name'].lower() == name.lower():
            print("This is the actual recipe:")
            console.print(Panel(show_recipe(recipe), border_style="magenta", title_align="left"))
            to_edit = input("Would you like to edit the name, the ingredients or the instructions? ")

            if to_edit.lower() == 'name':
                new_name = input("Please write the new name: ")
                recipe['name'] = new_name.strip()
            elif to_edit.lower() == 'ingredients':
                new_ingredients = input("Please write the new ingredients: ").split(',')
                recipe['ingredients'] = [ingredient.strip() for ingredient in new_ingredients]
            elif to_edit.lower() == 'instructions':
                new_instructions = input("Please write the new instructions: ")
                recipe['instructions'] = new_instructions.strip()
            print(f"The {recipe['name']}'s recipe has been successfully edited!")
            return

    print("The recipe you want to edit couldn't be found, you might have written the name wrong.")


def delete_recipe(recipes):
    name = input("Which is the name of the recipe you want to delete? ")

    for recipe in recipes:
        if recipe['name'].lower() == name.lower():
            recipes.remove(recipe)
            print("The recipe has been successfully removed!")
            return

    print("The recipe you want to edit couldn't be found, you might have written the name wrong.")


if __name__ == "__main__":
    main()
