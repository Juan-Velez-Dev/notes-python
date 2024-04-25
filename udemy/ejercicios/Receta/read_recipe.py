"""
esta el la opcion 1 de la linea de comandos
"""
from functions import command_user
from pathlib import Path
from os import system

categories = ['Carnes', 'Ensaladas', 'Pastas', 'Postres']


print("""
            Hola!, mi nombre es 'admintor' y soy tu manager de directorios
    """)
print("\n" + '*' * 100 + "\n")

# enseñamos en que ruta se encuentran las recetas


rute = Path(
    Path.home(), "Documents/code/NOTES/LANGUAJE/PYTHON/udemy/ejercicios/Receta/Recetas")

print(f"    La ruta de acceso es : {rute}")

# total de recetas de los directorios

total_recipes = len(list(rute.glob('**/*.txt')))
print('-'*100)
print(f"    El total de recetas en la ruta es de : {total_recipes}")


def print_categories(categories_list: list):
    print(f"Comandos de las categoria : \n")
    dict_categories = {i + 1: category for i,
                       category in enumerate(categories_list)}
    for k, v in dict_categories.items():
        print(f'Comando : [{k}] => {v}')
    return dict_categories


def find_categorie(categories):
    while True:
        categorie = ''
        user_command = command_user()
        if user_command in categories:
            categorie = categories[user_command]
            print(f"Haz seleccionado la categoria : [{categorie}]")
            print("\n" + '*' * 100 + "\n")
            return categorie
        else:
            print("Seleccione un comnado valido!!")


# def open_folder(rute, folder, )


def pick_category(categories_list: list, rute: Path):
    print("\n" + '*' * 100 + "\n")
    categories = print_categories(categories_list)
    categorie = find_categorie(categories)
    new_rute = rute / categorie
    return new_rute


def print_recipes(rute: Path):
    print("Lista de resetas : \n")
    recipes = [recipe for recipe in rute.iterdir() if recipe.is_file()]
    recipe_dict = {}
    for index, recipe in enumerate(recipes, start=1):
        recipe_dict[index] = recipe.name
    for index, recipe in recipe_dict.items():
        print(f'Receta : [{index}] => {recipe}')
    return recipe_dict


def find_recipe(recipes):
    while True:
        recipe = ''
        user_command = command_user()
        if user_command in recipes:
            recipe = recipes[user_command]
            print(f"Haz seleccionado la receta : [{recipe}]")
            print("\n" + '*' * 100 + "\n")
            return recipe
        else:
            print("Seleccione un comnado valido!!")


def pick_recipe(rute: Path):
    recipes = print_recipes(rute)
    print("Selecciona el comando de la receta que desas ver : ")
    recipe = find_recipe(recipes)
    return recipe


def show_recipe(rute: Path, recipe):
    recipe_to_show = rute / recipe
    with open(recipe_to_show, 'r') as recipe:
        recipe_instruction = recipe.read()
    print("\n" + '*' * 100 + "\n")
    print('Receta : ')
    print(recipe_instruction)


# def pick_recipe(rute: Path):
#     print("\n" + '*' * 100 + "\n")


def read_recipe():
    new_rute = pick_category(categories, rute)
    system('clear')
    recipe = pick_recipe(new_rute)
    system('clear')
    show_recipe(new_rute, recipe)
