class Creature:
    def __init__(self, name, food_level, needs_food_below, absorbs):
        self.name = name
        self.food_level = food_level
        self.needs_food_below = needs_food_below
        self.absorbs = absorbs

    def update_food_level(self, food):
        if self.food_level < self.needs_food_below:
            self.food_level += food * self.absorbs / 100

    def __str__(self):
        return f"Name: {self.name}, Food level: {self.food_level}, Needs food below: {self.needs_food_below}"