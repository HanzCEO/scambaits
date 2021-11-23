import random
from faker.providers import BaseProvider

hobbies = [
	'clash of clans', 'age of empire', 'age of empire 2', 'agar.io', 'slither.io', 'hole.io', 'state.io',
	'N/A'
]

class GameProvider(BaseProvider):
	def game(self):
		return random.choice(hobbies)
