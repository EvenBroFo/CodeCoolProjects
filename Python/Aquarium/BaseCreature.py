class BaseCreature:
    def __init__(self, name, food_level):
        self.name = name
        self.food_level = food_level

    def __str__(self):
        if self.needs_food():
            return f"The {self.name}, needs food"
        else:
            return f"The {self.name}, does not need food"