from user import User

class Moderator(User):

	total_mods = 0
	def __init__(self, first, last, age, community):
		super().__init__(first, last, age)
		self.community = community
		Moderator.total_mods += 1

	@classmethod
	def display_active_mods(cls):
		return f"There are currently {cls.total_mods} active moderators."

	def remove_post(self):
		return f"The moderator {self.full_name()} removed a post from the {self.community} community."


user1 = User("Malcolm", "Batista", 25)
user2 = User("Joe", "Rogan", 44)	
user3 = User("Jasmine", "Flores", 27)

mod1 = Moderator("Jas", "Ras", 22, "MMA Fans")
mod2 = Moderator("Louis", "Hammer", 36, "NBA Streams")

print(User.display_active_users())
print(Moderator.display_active_mods())