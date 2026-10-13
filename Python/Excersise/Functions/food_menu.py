def food_menu(food_items):
    menu = []

    for position, food in enumerate(food_items, start=1):
        menu.append(f"{position}. {food}")

    return menu


print(food_menu(["Hawaii Pizza", "Diablo Pizza"]))