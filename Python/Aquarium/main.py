from Aquarium import Aquarium
from Plant import Plant
from Fish import Fish 

aquarium = Aquarium()

goldfish = Fish("Goldfish", 5)
clownfish = Fish("Clownfish", 3)
seaweed = Plant("Seaweed", 0)
kelp = Plant("Kelp", 0)

aquarium.add_creature(goldfish)
aquarium.add_creature(clownfish)
aquarium.add_creature(seaweed)
aquarium.add_creature(kelp)

print("Before feeding:")
aquarium.display_details()
print("After feeding 50:")
aquarium.feed(50)
aquarium.display_details()
print("After feeding 80:")
aquarium.feed(80)
aquarium.display_details()
