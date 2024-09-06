# The Kitten's Recipe Book - A Recipe Manager Application
#### Video Demo:  [Watch the Video](https://youtu.be/t1ACrHC4kZQ)
#### Description:

The Kitten's Recipe Book is a Python-based console application that helps users manage their recipes. Users can add, view, edit, delete, and generate shopping lists based on their saved recipes. The project is designed to simplify the process of organizing ingredients and instructions for various dishes.

The app aims to solve the problem of recipe management by providing an easy-to-use interface where users can store and retrieve their favorite recipes. It is ideal for anyone who loves cooking and wants to keep their recipes organized (like myself).

## Features:
- **Add Recipes**: Allows users to input new recipes with ingredients and instructions.
- **View Recipes**: Displays a list of all saved recipes and allows users to see details.
- **Edit Recipes**: Users can edit the details of a recipe, including its ingredients and instructions, if they wish to update or correct it.
- **Delete Recipes**: Users can delete recipes they no longer need.
- **Shopping List Generator**: Automatically generates a shopping list based on the ingredients from multiple recipes.

## Files:

### 1. `project.py`
This is the main Python file that contains the core logic of the application. It handles user inputs and calls the appropriate functions to add, view, edit, or delete recipes. Additionally, it manages the shopping list generation feature.

### 2. `requirements.txt`
This file lists the dependencies required for the project to run. It ensures that all the necessary libraries are installed. Key dependencies include:

- `rich`: Used for enhanced console output with better formatting.
- `pytest`: A testing framework used for testing the application.

### 3. `test_project.py`
This file contains the unit tests for the project. It uses pytest to ensure that all core functions, such as adding, editing, deleting recipes, and generating the shopping list, work as expected. The test coverage includes:

- `Testing recipe addition`: Ensures that new recipes are correctly added.
- `Testing recipe deletion`: Ensures that recipes are properly deleted.
- `Testing recipe editing`: Verifies that existing recipes can be modified.
- `Testing shopping list generation`: Confirms that the shopping list is generated accurately from the recipes.

## Design Decisions:

The decision to implement the project using Python was driven by the simplicity and readability of the language. The `rich` library was used to improve the console's UI by adding color and formatting to make the output more user-friendly.

I debated between storing the recipes in a database or in memory. Ultimately, I chose in-memory storage for simplicity, but future versions might include database integration for persistence.

## Challenges:

One of the main challenges was handling user input validation to ensure that only valid recipes were added to the application. I also had to work through designing a flexible system for the shopping list generation feature and ensuring users could effectively edit recipes.

## Future Enhancements:

- Add support for storing recipes in a database for long-term persistence.
- Implement a web interface for better accessibility.
- Allow users to categorize recipes by type (e.g., breakfast, lunch, dinner).

## Conclusion:

This project provided an excellent opportunity to practice Python and console-based UI design. It was challenging but rewarding to implement features like shopping list generation and recipe editing. I believe this tool could be highly useful for home cooks looking for a digital way to manage their recipes.
