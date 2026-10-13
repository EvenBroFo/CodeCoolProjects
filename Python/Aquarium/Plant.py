from BaseCreature import BaseCreature

class Plant(BaseCreature):

    def __init__(self, name, food_level):
        super().__init__(name, food_level)

    def needs_food(self):
        return self.food_level < 15 

    def absorb_food(self, food_amount):
        self.food_level += food_amount * 0.5

    

