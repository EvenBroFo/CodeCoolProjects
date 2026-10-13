class Aquarium:
    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def display_details(self):
        for creature in self.creatures:
            print(creature)

    def feed(self, food_amount):
        hungry_creatures = []
        for creature in self.creatures:
            if creature.needs_food():
                hungry_creatures.append(creature)
        if len(hungry_creatures) > 0:
            food_for_each = food_amount / len(hungry_creatures)
            for creature in hungry_creatures:
                creature.absorb_food(food_for_each)
        print(f"Feeding with {food_amount}")
        