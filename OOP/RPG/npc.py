from character import Character

class NPC(Character):

	def __init__(self, name, hp, level):
		super().__init__(name, hp, level)

	def speak(self):
		print("I heard there were monsters running around last night!")

villager = NPC("Dann", 120, 3)
print(villager.name)
print(villager.hp)
print(villager.level)
villager.speak()